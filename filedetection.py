# Python file detection

import os #os means operation system. 

file_path = "stuff/file.txt" # If you want to use \ you need to use \\ instead, or you can use only /. ex:  C:\\Users\\flavi\\OneDrive\\Área de Trabalho\\project\\stuff\\file.txt -- C:/Users/flavi/OneDrive/Área de Trabalho/project/stuff/file.txt

if os.path.exists(file_path):
    print(f"The location {file_path} exists")
    
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")