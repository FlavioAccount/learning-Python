# Python writing files (.txt, .json, .csv)

import json
import csv

txt_data = "I like pizza! "

file_path = "output.txt"
file_json = "outputjson.json"
file_csv = "outputcsv.csv"


# In the following syntax, 
# "w" means write. 
# "x" is also write, but it is used case the file doesn't exist. 
# "a" is used to append the file. 
# "r" is used to read the file
# OBS:Is not required to write (file=, mode=)
employees = ["Eugene", "Squidward", "Spongebob", "Patrick"] #txt example
people = {
    "name": "Spongebob",
    "age": 30,
    "Job": "cook"
} #csv example
people_csv = [["Name", "age", "job"],#First row
              ["Spongebob", "30", "Cook"],
              ["Patrick", "37", "Unemplyed"],
              ["Sandy", "27", "Scientist"]]

try:
    with open(file=file_path, mode="w") as file: #When we open the file, it will be closed automatically after running the script
        file.write(txt_data)
        print(f"txt file '{file_path}' has been created")
except FileExistsError:
    print("That file already exists!")
try:
    with open(file=file_path, mode="a") as file: #When we open the file, it will be closed automatically after running the script
        file.write("\nThis string has been added using file.write()")
        for employee in employees:#If you try to write everything inside the employees list, it is not going to write it because the write only accepts strings
            file.write("\n" + employee)
except FileExistsError:
    print("That file already exists!")

#I am gonna create a json file

try:
    with open(file_json, "w") as filejson:
        json.dump(people, filejson, indent=4) #This method will convert a dictionary to a json method. indent will create 4 spaces for each line
        print(f"json file '{file_json} has been created")
except FileExistsError:
    print("That file already exists!")

#We will work with csv files now (CSV = comma separated values)

try:
    with open(file_csv, "w",newline="") as filecsv:
        writer = csv.writer(filecsv) #This method will convert a dictionary to a json method. indent will create 4 spaces for each line
        for row in people_csv:
            writer.writerow(row)
        print(f"csv file '{file_csv}' has been created")
except FileExistsError:
    print("That file already exists!")

