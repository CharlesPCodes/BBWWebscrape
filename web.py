from bs4 import BeautifulSoup
from urllib.request import urlopen
import smtplib
from datetime import datetime
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


########################################### ONLY CHANGE WHATS BELOW #############################################
fromaddr = "" #This is going to be the email address that the text file is sent from
toaddr = "" #The to address that the text file is sent to. Will try to make a database of emailsa for the script to run through

#Below change the current dir to where the text file is located
#In order to move up in a folder make sure you have the \\ otherwise it won't move up
fileLocation = "C:\\Desktop\\FinalOutput.txt"


#Below change the login username and password for the sender email.
#NOTE :: You may need to allow login when using gmail for security purposes
senderEmail = ""
senderPassword = ""
#################################################################################################################


# Sets url to bbw var
bbw = 'http://www.bathandbodyworks.com/g/top-offers'
#opens page
page = urlopen(bbw)
#parses the open html 
soup = BeautifulSoup(page, 'html.parser')

# finds all divs with the class of banner-container and saves it into a variable

'''
NOTE: FOR ANY ISSUES REGARDING NOT RECIEVING AN EMAIL.
DEV: If no more emails, check to see if the cells names have changed or if sender email is blocking for security reasons--- from google
'''
col_one = soup.find_all('div', attrs={'class' : 'banner-container clearfix two-cells'})[0]
print(col_one.text)

col_two = soup.find_all('div', attrs={'class' : 'banner-container clearfix two-cells'})[1]
print(col_two.text)

col_three = soup.find_all('div', attrs={'class' : 'banner-container clearfix two-cells'})[2]
print(col_three.text)

col_four = soup.find_all('div', attrs={'class' : 'banner-container clearfix two-cells'})[3]
print(col_four.text)

#This removes the text file so it can be re-written
os.remove("FinalOutput.txt")

#opens text file and prints the saved deals to the text document
with open('FinalOutput.txt', "w") as text_file:
	print(col_one.text.strip(), file=text_file)
	print(col_two.text.strip(), file=text_file)
	print(col_three.text.strip(), file=text_file)
	print(col_four.text.strip(), file=text_file)

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Bath and Body Works Top Offers %s" % datetime.now()
body = ("BBW Top Offers")

msg.attach(MIMEText(body, 'plain'))

# Sets the file name and sets the location of the file
filename="FinalOutput.txt"
attachment = open(fileLocation, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(senderEmail, senderPassword)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


