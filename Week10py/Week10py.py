# Assignee: Skyler Millburn
# Assignment: 10.1
# Date: 21 FEB 2021
# Description: Gets information from the user before writing to a file. Then prints out what is in the file
import os

name = ""
address = ""
phone = ""

# Check if the directory already exists
def verifyDirectory(directory):
    if (os.path.isdir(directory)):
        print("Directory Exists. Continuing program.")
        return True
    else:
        print("Directory does not exist. Exiting program.")
        return False

# Check if file exists. If it does exist fall through program to exit. 
def verifyFile(path):
    if (os.path.exists(path)):
        print("File already exists. Exiting program.")
        return True
    else:
        print("File does not already exists. Continuing program.")
        return False

# Get the file information from the user
def getFileInfo():
    directory = input("Enter a directory to save the file: ")
    # Only continue if the directory exists.
    if(os.path.isdir(directory)):
        filename = input("Enter a filename for your file: ")
        path = os.path.join(directory, filename)
        # Do not continue if the file already exists. Don't want to overwite files at the moment
        if(os.path.exists(path)):
            print("File already exists. Exiting program.")
        else:
            getUserInfo()
            os.chdir(directory)
            saveCSV(filename)
            verifyOutput(filename)
    else:
        print("Directory does not exist. Exiting program.")

# Gets user input for information
def getUserInfo():
    global name
    name = input("Name: ")
    global address
    address = input("Address: ")
    global phone
    phone = input("Phone Number: ")

# Save information in a comma seperated format
def saveCSV(file):
    try:
        with open(file, "w") as text_File:
            text_File.write(name + "," + address + "," + phone)
    except:
        print("Could not write to file")

# Print out everything in the file
def verifyOutput(file):
    try:
        file = open(file, "r")
        print(file.read())
    except:
        print("Could not open file")

getFileInfo()