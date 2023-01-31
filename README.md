## CS50x Introduction to Computer Science
This is Harvard University's (HarvardX's) introduction to the intellectual enterprises of computer science and programming provided on Coursera learning platform. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, Python, SQL, and JavaScript plus CSS and HTML. The study load of the course is approximately 180 hours.

### Key Competences 
The participants of this course learn:
* A broad and robust understanding of computer science and programming
* How to think algorithmically and solve programming problems efficiently
* Concepts like abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development
* Familiarity in a number of languages, including C, Python, SQL, and JavaScript plus CSS and HTML
* How to develop and present a final programming project to the peers

For more info see <https://www.edx.org/course/introduction-computer-science-harvardx-cs50x>.

<br>

### Final Project 
This GitHub repository stores my solution for the final project of the CS50's Introduction to Computer Science demonstrating practical skills in programming. This project was submitted in November 2022 and is constructed with the following programming languanges / technologies:
- python (PyCharm)
- sql 
- html
- css
- javascript
- jinja

The following external libraries are used in Python: selenium, bs4, re, time, pandas, sqlite3, flask, cs50 and time.

#### Project Summary
##### Part 1: 
The program is written in python and web scrapps the key information about available apartments from a property company's website. The code accesses the company's website and accepts the cookies with the chromedrive and uses the soup library to read the information from the html code, namely the table with the basic apartment information. Then it accesses the hyperlinks in the main html table to find and store more details into the computer's memory as panda dataframe. Also the code transforms the data from the website into the needed format and structure.

##### Part 2: 
In this part the program creates a .db file with one sql table via the sqlite3 library to save all the collected data in the SQL database.

##### Part 3: 
In the last part the python code creates a simple overview website with three pages. The first page is the homepage. The second page is the advisory page including links to external websites about finding a good apartment. Finally, the third page is the result page summarizing all the scrapped information with hyperlinks to the individual apartmants from the original property company's website.

