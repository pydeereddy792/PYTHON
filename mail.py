# program to send email through coding

import smtplib
import getpass

myemail=input("your email id : ")
password=getpass.getpass()
recemail= input("recievers email id :")

#creating smtp session
s = smtplib.SMTP('smtp. gmail.com', 587)

#start tls for security
s.starttls()
#authentication
s.login(myemail,password)

message = " message need to be sent"
s.sendmail(myemail,recemail,message)

s.quit()