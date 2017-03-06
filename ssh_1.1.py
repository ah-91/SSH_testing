import sys
import paramiko
import datetime
import time
import smtplib

#Storing output in a file for  logs locally 
file = open("ssh_connection.txt",'a')
sys.stdout = file


current_time = datetime.datetime.now()
print ("\n")
print (current_time , "\n")

s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

L = ["list of ports seperated by commas"]

decoded_string_list=[]    #Creating a Empty List for sending the result all together 

# Enter the hostname of the server to be connected and username ,password
for i in L:
	s.connect(hostname = "",port=i, username="", password="")
	channel = s.invoke_shell()
	if channel.closed :
		print("Connection dead")
	else:
		print("port",i,"-Connection alive")
		print ("\n")
		channel.send("\n")
		time.sleep(30)                       #Waiting for prompt to appear 
		prompt = channel.recv(999)			 

#Decoding part as the result received were in byte array ,therefore have to convert into string 	

#		prompt_decoded = str(prompt)
#		decoded_string = bytes(prompt_decoded, "utf-8").decode("unicode_escape")
		decoded_string1 = prompt.decode("unicode_escape")
#		print(decoded_string1)
		decoded_string_list.append(decoded_string1)
		


a = "1st port"+"\n"+decoded_string_list[0].strip()
b = "2nd port"+"\n"+decoded_string_list[1].strip()
c = "3rd port"+"\n"+decoded_string_list[2].strip()
d = "4th port"+"\n"+decoded_string_list[3].strip()

result =a+"\n" +"\n" +b+"\n"+"\n"+c+"\n"+"\n"+d   #Human readable format 


#Adding FROM,  TO , SUBJECT, result as a header

FROM="" #Enter the From field to be dsipalyed 

SUBJECT ="" #Enter the Subject to be displayed 
TO="" #Enter the TO field to be displayed

Output = "FROM: {}\nTO: {}\nSubject: {}\n\n{}".format(FROM,TO,SUBJECT, result)

s = smtplib.SMTP('smtp.gmail.com', 25)
s.starttls()
s.ehlo()
s.login("username" , "password") #Login to gmail server  
s.sendmail('From', 'to', Output)


s.close()
file.close()


