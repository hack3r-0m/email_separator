import os
import sys


fileName = input("Enter File Name :") # ONLY WORKS IF EMAIL FILE IS IN SAME DIRECTORY AS OF PYTHON


if os.path.exists(fileName) == False :
    print("FILE NOT FOUND") 
    print("PLEASE KEEP YOUR EMAIL FILE IN SAME FOLDER OF THIS FILE")
    print("PLEASE ADD FILE WITH PROPER EXTENSION")
    exit()

open_file = open(fileName, "r", encoding='utf-8')
lines_converted = open_file.readlines()
open_file.close()

for i in range(len(lines_converted)):
    lines_converted[i] = lines_converted[i].rstrip()
    lines_converted[i].split("@")

    print("[{}] ".format(i+1) + lines_converted[i].rstrip() )

    if lines_converted[i].split("@")[1] == "outlook.com" :
        outlook = open("emails_outlook.txt","a+")
        outlook.writelines(lines_converted[i].rstrip() + "\n")

    elif lines_converted[i].split("@")[1] == "gmail.com" :
        gmail = open("emails_gmail.txt","a+")
        gmail.writelines(lines_converted[i].rstrip() + "\n")

    elif lines_converted[i].split("@")[1] == "yahoo.com" :
        yahoo = open("emails_yahoo.txt","a+")
        yahoo.writelines(lines_converted[i].rstrip() + "\n")

    elif lines_converted[i].split("@")[1] == "aol.com" :
        aol = open("emails_aol.txt","a+")
        aol.writelines(lines_converted[i].rstrip() + "\n")
    else :
        other = aol = open("emails_other.txt","a+")
        other.writelines(lines_converted[i].rstrip() + "\n")

print("ALL EMAILS CHECKED SUCCESSFULLY!")
print("COPYRIGHTS")
print("CREATED BY HACK3R_0M")
