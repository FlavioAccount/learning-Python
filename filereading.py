# Python reading files (.txt, .json, .csv)
# 'r' means the open method will read the file

import json #You need to import the json library to use it
import csv

file_path = "C:\\Users\\flavi\\OneDrive\\Área de Trabalho\\project\\output.txt"
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file has not been found")
except PermissionError: #This exception is added case the document is not available for reading
    print("You do not have permission to read that file")

#If you want to read a json file, you need to import the json library first

file_json = "C:\\Users\\flavi\\OneDrive\\Área de Trabalho\\project\\outputjson.json"
try:
    with open(file_json, "r") as file1:
        jsonfile = json.load(file1)
        print(jsonfile["name"]) #You can access the jsonfile by its keyword
except FileNotFoundError:
    print("File doesn't exist")
except PermissionError:
    print("Cannot open the file, permission denied!")

file_csv = "C:\\Users\\flavi\\OneDrive\\Área de Trabalho\\project\\outputcsv.csv"

try:
    with open(file_csv, "r") as filecsv:
        csvfile = csv.reader(filecsv) #It will return a address of data. If you want to load the full data, you need to iterate 
        for line in csvfile:
            print(line)
        print(csvfile)
except FileNotFoundError:
    print("File doesn't exist!")
except PermissionError:
    print("Permission denied! The file is blocked")
