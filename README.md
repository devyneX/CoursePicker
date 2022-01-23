# Course Picker
A desktop app to check the unlocked courses bases on previously done courses. 

## Table of contents
---
* [About the Project](#about-the-project)
* [Built with](#built-with)
* [What it does](#what-it-does)
* [How to use](#how-to-use)


## About the Project
---
It's a simple project I made while doing preadvising. The open credit system can be somewhat hectic at times. Even if you have a course tree, you need to check that manually and find the courses that you have been unlocked. So being a programmer, I thought why not automate the damn thing and be done with it. Of course, that wasn't easy either 😅 But hey, at least, now I was doing something I like, right? 

It will only work for CSE students of BRACU, but feel free to pull and change up to fit your University. 

## Built with 
---
* python
* pandas 
* tkinter

## What it does
---
By inputting the courses you've done so far, you can get a list of courses you've unlocked and can choose from. 

## How to use
---
Completed courses can be inputted using
* the checkboxes
    - pretty self-explanatory, check the completed courses and click the submit button at the bottom

* a .txt file
    - list the completed courses in a .txt file, one in a line. Check the completed_courses.txt file in the repo to get an idea.
    - click the folder icon next to .txt input box to browse to this file and select
    - click the submit button next to it
* a .csv file 
    - copy completed_courses.csv and paste it somewhere.
    - edit the copied file and type "YES" in the FINISHED column of the completeed courses.
    - click the folder icon next to .csv input box to browse to this file and select
    - click the submit button next to it

> may show irregularities if in the input, there's a completed course whose prerequisite wasn't done. For example, if CSE221 was checked but CSE220 wasn't checked. 

---

Feel free to let me know if you find any bugs or if you have any suggestions for improvements or additional features.
