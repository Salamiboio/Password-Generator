import string
import random
import os
from pathlib import Path

#defines
home = os.path.expanduser('~')#makes home point to home directory
app_for = input("What is this for: ")
length = int(input("Enter the length of password: "))
special_in = input("What Special Characters are allowed?: ")
special = tuple(special_in.split())#takes special_in input, splits it and makes it a tuple
charList = string.ascii_letters + string.digits #Puts letters and numbers into the charList
p_final = [] #final password character list

for x in special: #Runs through special characters and adds them to charList
    charList += x

for x in range(length): #Uses the length int to choose a set amount of characters from charList

   p = random.choice(charList)
   p_final.append(p) #takes choices and puts them into list

password = "".join(p_final) #makes password list into an actual password

password_file = f"{home}\\documents\\passwords.txt"
path_exist = os.path.exists(password_file) #detects if you have a passwords.txt file
if path_exist == False:
           Path(password_file).touch() #if not creates one for you

f = open(password_file, "a") #adds password to password.txt
f.write(f"{app_for} = {password}\n")
f.close()