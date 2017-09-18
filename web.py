from bs4 import BeautifulSoup
from urllib.request import urlopen
import smtplib
from datetime import datetime
import os

bbw = 'http://www.bathandbodyworks.com/g/top-offers'
page = urlopen(bbw)
soup = BeautifulSoup(page, 'html.parser')


col_one = soup.find_all('div', attrs={'class' : 'banner-container clearfix three-two'})[0]
print(col_one.text)


col_two = soup.find_all('div', attrs={'class' : 'banner-container clearfix three-two'})[1]
print(col_two.text)

col_three = soup.find_all('div', attrs={'class' : 'banner-container clearfix three-two'})[2]
print(col_three.text)

col_four = soup.find_all('div', attrs={'class' : 'banner-container clearfix three-two'})[3]
print(col_four.text)



os.remove("FinalOutput.txt")





with open('FinalOutput.txt', "w") as text_file:
	print(col_one.text.strip(), file=text_file)
	print(col_two.text.strip(), file=text_file)
	print(col_three.text.strip(), file=text_file)
	print(col_four.text.strip(), file=text_file)





##############################
# email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#FROM ADDRESS HERE
fromaddr=""
# TO ADDRESS HERE
toaddr=""

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Bath and Body Top Offers %s" % datetime.now()
body = ("BBW Top Offers")


msg.attach(MIMEText(body, 'plain'))

filename="FinalOutput.txt"
#CHANGE DIRECTORY TO WHERE TEXT FILE IS SAVED
attachment = open("", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#EMAIL ACCOUNT LOGIN
server.login()
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


