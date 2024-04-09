import string
import random
import os
from pathlib import Path

home = os.path.expanduser('~')
app_for = input("What is this for: ")
length = int(input("Enter the length of password: "))
special_in = input("What Special Characters are allowed?: ")
special = tuple(special_in.split())
charList = string.ascii_letters + string.digits
p_final = []

for x in special:
    charList += x

for x in range(length):

   p = random.choice(charList)
   p_final.append(p)

password = "".join(p_final)

password_file = f"{home}\\documents\\passwords.txt"
path_exist = os.path.exists(password_file)
if path_exist == False:
           Path(password_file).touch()

f = open(password_file, "a")
f.write(f"{app_for} = {password}\n")
f.close()