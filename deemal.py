# program to send email through coding

import smtplib
import getpass

myemail=input("your email id : ")
password=getpass.getpass()
recemail= input("recievers email id :")

#creating smtp session
s = smtplib.SMTP('smtp.gmail.com', 587)

#start tls for security
s.starttls()
#authentication
s.login(myemail,password)

message = 
import matplotlib. pyplot as plt 
import csv 
x=[]
y=[]
with open('/home/cl302/deepthireddy/n.csv','r')as csvfile:
	plots= csv.reader(csvfile,delimiter=',')
	for row in plots:
 		x.append(int(row[0]))
 		y.append(int(row[1]))

plt.plot(x,y, label='loaded from file!')
plt.xlabel ('x axis')
plt.ylabel ('y axis')
plt.title('my test result')
plt.legend()
plt.show()

s.sendmail(myemail,recemail,message)

s.quit()