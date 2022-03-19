"""
    File: listFiles.py
    Print all of the names of files in the current 
    working directory with a .py extention
"""
import os

currentDirectoryPath = os.getcwd()
listOfFileNames = os.listdir(currentDirectoryPath)
for name in listOfFileNames:
    if ".py" in name:
        print(name)