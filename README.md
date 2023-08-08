# CODSOFT
All the projects that I have done as the part of CODSOFT internship program in Python programming language 

# Calculator
libraries used: Tkinter  
it is a GUI toolkit with the help of which the GUI-based application can be made.
functions made are: values(), calculate(), clear()
values() -> this functions takes all the characters that are input by the user is taken 
calculate() -> the calculation is done inside this function 
clear() -> used to delete the strings that are in the entry field already.

# Password generator
libraries used: tkinter, random, pyperclip, string
tkinter for creating GUI applications.
random for randomly selecting the integers or from the set of given values.
pyperclip for copying the string to the clipboard.
string for working with strings.

Input is taken from the user in the form of the password length as the length of the password must be in the limits that are specified by the user.
The input is given with the help of the prompt.

functions used are: generate(), copy()
generate() -> generating the password by randomly choosing the lowercase, uppercase, digits and punctions and creating a totally random string.
in this all the possible characters are accessed using the ascii like:
ascii_lowercase includes all the lowercase letters such as a,b,c,d,e,f
ascii_uppercase includes all the uppercase letters such as A,B,C,D,E,F
the empty string is made named as password in which all the characters are joined in this variable. 
cop() -> inside this function with the help of pyperclip the randomly generated string is copied to the clipboard

# Todo app:
libraries used: Tkinter 
The task is taken as input from the user and saved as a list along with that some functions like updating the task, removing the task, and deleting all tasks from the list.
functions made are: addition(), removing(), updating(), clearing()
addition() -> adding the input task from the user and saving it in a list of tasks. 
this function is called by the (Add Task) button.
removing() -> deleting the selected task from the list of tasks.
this function is called by the (Remove Task) button.
updating() -> updating the task with the value that is entered in the Entry() field.
this function is called by the (Update Task) button.
clearing() -> to delete all the tasks from the list 
this function is used by the (Clear All) button.
