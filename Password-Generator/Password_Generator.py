import string
import random
import os
from pathlib import Path
import email
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import pyminizip

#passwords
app_password = "" #Get app password from google account
zip_password = "" #Password for your zip file

sender = "" #Your gmail
recipients = [""] #Gmails of recipients

#defines
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
home = os.path.expanduser('~')#makes home point to home directory
app_for = input("What is this for: ")
length = int(input("Enter the length of password: "))
special_in = input("What Special Characters are allowed?: ")
special = tuple(special_in.split())#takes special_in input, splits it and makes it a tuple
charList = string.ascii_letters + string.digits #Puts letters and numbers into the charList
p_final = [] #final password character list
source_dir = f"{home}\\documents\\"
password_file = f"{source_dir}passwords.txt" #where password is stored

for x in special: #Runs through special characters and adds them to charList
    charList += x

for x in range(length): #Uses the length int to choose a set amount of characters from charList
   p = random.SystemRandom().choice(charList)
   p_final.append(p) #takes choices and puts them into list
password = "".join(p_final) #makes password list into an actual password

with open(password_file, 'a') as file: #adds password to text file, if it doesn't exist it creates the text file
    file.write(f"{app_for} = {password}\n")

pyminizip.compress(password_file, "", f"{source_dir}/passwords.zip", zip_password , int(1)) #Creates password locked zip file

#Message contents
now = datetime.now()
subject = f"Passwords Changed at {now}"
body = ""

#sends the email
def send_email(subject, body, sender, recipients, app_password):
    msg = email.mime.multipart.MIMEMultipart(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    body = email.mime.text.MIMEText(f"The passwords file had new passwords added at {now}")
    msg.attach(body)
    filename= f"{source_dir}passwords.zip"
    with open(filename, "rb") as fs:
        part = MIMEBase('application', "octet-stream")
        part.set_payload(fs.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filename))
    msg.attach(part)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, app_password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, app_password)
