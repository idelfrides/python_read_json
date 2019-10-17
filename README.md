# Handle json documents with python

### The Project
This is a project created to **handle json files to mutables data structures** in Python 3. 
It is a solution to a challenge. This is the practical test for my admission in my second job as a backend developer.

This project is about managing text file containing json document in python.
On it I build an app witch get data in a json file and  put it into a mutable data structure chosen by user/you trough a menu of selection. 
The App use **OOP** and **Microserce Architecture** and organized like you can see on tab **<> Code** (in the top left menu).
- The folder **handle_json_files** is a python package witch contain modules(classes, python files). Each module keeps some methods, where each method is responsible to execute one task. The classes  has the same name with python file.
- The folder **files_dir** keeps the files created by user and can be deleted anytime he want. 
So,  That is a structure seted up to satisfy the  **Microserce Architecture** adopted .

The file **main.py** has one method, the main one, called - **main_test()** wich one controlls the app fully.

### Running App
To run this app you need to execute **main.py** file.

----------------------
   ### The Challenge


The CHALLENGE consist in read a content from a json file('test.json' to our purpose) 
without using the 'loads()' method from json package. 
The CHALLENGE itself is only a reproduction of what the python function json.loads() does.

-------------------
   ### The Solution

The technique used to solve this CHALLENG is - reading the documents character by character,
to recover the test.json file content to a python variables.
The test.json file is only an example, the most important thing here is
that the script be able to work with other files in json format,
with different data structures, so the script must be dynamic.



-------------

Author: IDELFRIDES JORGE | Mail me by idelfridesjorge@alu.ufc.br 

FOLLOW ME ON GITHUB: [ENG. IDELFRIDES JORGE](https://github.com/idelfrides)
