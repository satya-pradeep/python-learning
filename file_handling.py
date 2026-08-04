#file handling
#File handling in Python refers to the process of storing, reading, writing, and managing data in files permanently on a storage device

#step 1: opening the file
#step 2: performing operation
#step 3: closing the operation

#The open() function takes two parameters; filename, and mode.

#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

#"a" - Append - Opens a file for appending, creates the file if it does not exist

#"w" - Write - Opens a file for writing, creates the file if it does not exist

#"x" - Create - Creates the specified file, returns an error if the file exists

#Syntax
#f = open("demofile.txt", "r")

#open a file
'''p = open("77492","r")
print(p.read())'''

#using with statement
'''with open("77492") as p:
    print(p.read())
'''

#Close Files
'''p = open("77492",'r')
print(p.read())
p.close()
'''

#Read Only Parts of the File
'''with open("77492") as p:
    print(p.read(7))
p.close()'''

#Read Lines
'''p = open("77492","r")
print(p.readline())
print(p.readline())
p.close()'''

'''with open("77492") as p:
    for i in p:
        print(i)'''

#Write to an Existing File
#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content
'''
with open("77492","a") as p:
    p.write("now the file has more content")

with open("77492") as p:
    print(p.read())'''

#Overwrite Existing Content
'''with open("77492","w") as p:
    p.write("woops i have deleted the content!")
with open("77492","r") as p:
    print(p.read())
'''

#Create a New File
'''p = open("pradeep","x")'''


#Delete a File
'''import os
os.remove("pradeep")'''

#Check if File exist:
"""import os
if os.path.exists("pradeep"):
    os.remove("pradeep")
else:
    print("the file does not exist")"""


#Delete Folder
#To delete an entire folder, use the os.rmdir() method:



