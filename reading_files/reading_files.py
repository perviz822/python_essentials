import os
print(os.getcwd())

file1 =   open("words.txt", "r") 
file2 =   open("words.txt", "w")
#reading5

with open("words.txt","r") as file2:
    file_stuff = file2.readlines(6)
    print(file_stuff)   






