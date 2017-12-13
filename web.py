from bs4 import BeautifulSoup
from urllib.request import urlopen
import smtplib
from datetime import datetime
import os


# Sets url to bbw var
bbw = 'http://www.bathandbodyworks.com/g/top-offers'
#opens page
page = urlopen(bbw)
#parses the open html 
soup = BeautifulSoup(page, 'html.parser')

# finds all divs with the class of banner-container and saves it into a variable

# NOTE:
# DEV: If no more emails, check to see if the cells names have changed
# 
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





##############################
# email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#gets the from address and the recipiant address


#####################################
# FOR USERS FILL IN THE EMAILS BELOW
fromaddr="FROMADDRESS"
toaddr="TOADDRESS"
#####################################
msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Bath and Body Top Offers %s" % datetime.now()
body = ("BBW Top Offers")


msg.attach(MIMEText(body, 'plain'))

filename="FinalOutput.txt"
#####################################
# CHANGE THE LOCATION OF WHERE YOUR FinalOutput.txt file is
attachment = open("C:", "rb")
#####################################
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)


# DONT CHANGE FOR GMAIL ONLY CHANGE WHAT IS IN THE #####
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#####################################
server.login('EMAIL', "PASSWORD")
#####################################
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


