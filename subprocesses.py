# Import libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from time import *
import pandas as pd
import sqlite3

# Define webscrapping function
def webscrap():
    # Set up chrome browser
    chromedriver = r'C:\Users\Martin\PycharmProjects\FlatBot\chromedriver.exe'
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(chromedriver, options=options)

    # Define url and open it in the browser
    url = str("https://www.xxxx.xx")
    browser.get(url)
    sleep(2)

    # Accept cookies
    browser.find_element("xpath", "//*[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']").click()
    sleep(2)

    # Scrap the data
    soup = BeautifulSoup(browser.page_source, "html.parser")

    # Find the relevant part of the table and format it to one list
    output_html = soup.find_all("td")
    output_list = []
    for j in range(82, len(output_html)):
        output_list.append(soup.find_all("td")[j].get_text().replace("\n", "") \
                           .replace("\t", "").replace("\xa0", " ").replace("€ ", "") \
                           .replace(", ", "; ").replace(".", "").replace(",", "."))

    # Split the list into sublists via function
    def divide_chunks(l, n):
        for m in range(0, len(l), n):
            yield l[m:m + n]

    output_lists = list(divide_chunks(output_list, 5))

    # Separate zip codes and street into two columns
    for z in range(0, len(output_lists)):
        output_lists[z] = output_lists[z][0].split(";") + output_lists[z][1:]

    # Use lists to crease data frame
    output_table_SB = pd.DataFrame(output_lists,
                                   columns=['District', "Address", 'Number_rooms', 'Equity', 'Rent', 'Lage'])
    output_table_SB = output_table_SB.drop(columns="Lage")

    # Insert new column for area and for website
    output_table_SB.insert(3, "Area", "NaN", True)
    output_table_SB = output_table_SB[['District', "Address", 'Number_rooms', "Area", 'Rent', 'Equity']]
    output_table_SB.insert(6, "Website", "NaN", True)

    # Scrap more data
    url_pages = []
    areas = []
    for i in range(0, len(output_table_SB)):
        dyn_xpath = "//*[@id='c115']/div/form/table/tbody/tr" + str([i+1]) + "/td[1]/a"
        element = browser.find_element("xpath", dyn_xpath)
        element.click()
        sleep(3)

        soup = BeautifulSoup(browser.page_source, "html.parser")
        area_html = soup.find("li", text=re.compile(r"m²"))
        area = area_html.get_text()
        area = area.replace("m²", "")
        areas.append(str(area))

        url_pages.append(browser.current_url)

        url = str("https://www.xxxx.xx")
        browser.get(url)

    # Create first output table from addresses and prices (each vector is one column)
    output_table_SB["Website"] = url_pages
    output_table_SB["Area"] = areas
    pd.set_option('display.expand_frame_repr', False)  # show all columns
    pd.set_option('max_colwidth', 20)  # set up the width of columns
    print(output_table_SB)

    # Output the data into csv if desired
    # output_table_SB.to_csv("opt_SB_data.csv", encoding="iso-8859-15")

    # Close chrome
    browser.quit()

    return output_table_SB


# Create function to transfer the panda data frame into sqlite3
# Code used partially comes from https://datatofish.com/pandas-dataframe-to-sql/
def sqlite_database(output_table_SB):
    # Create new file
    sql_name = "sqlite_database.db"
    conn = sqlite3.connect(sql_name)
    c = conn.cursor()

    # Create new table
    c.execute('CREATE TABLE IF NOT EXISTS apartments (Id, District, Address, Number_rooms, Area, Rent, Equity, Website)')
    conn.commit()

    # Copy the data from panda data frame into sqlite table
    df = pd.DataFrame(output_table_SB, columns= ['Id','District', 'Address', 'Number_rooms', 'Area', 'Rent', 'Equity', 'Website'])
    df.to_sql('apartments', conn, if_exists='replace', index = False)

    # Print the data from sqlite3 file if desired
    # c.execute('''SELECT * FROM apartments''')
    # for row in c.fetchall():
    #    print(row)