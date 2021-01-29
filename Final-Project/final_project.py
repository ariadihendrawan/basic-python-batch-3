#Ref : https://realpython.com/python-send-email/
#Ref : https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python
#Ref : https://stackoverflow.com/questions/6270782/how-to-send-an-email-with-python
#Ref : https://stackoverflow.com/questions/28795247/masking-keyboard-input-with-a-character-python-version-3-0

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import getpass

print("================================")
print("PROGRAM KIRIM EMAIL DENGAN GMAIL")
print("================================")
fromaddr = input("Login to Gmail Account   : ")
pswd = getpass.getpass("Masukkan password        : ")

n=int(input("Masukkan jumlah penerima : "))
f=open("receiver_list.txt","w")

daftar_email=[]
for x in range(n):
    tambah=input("Masukkan email penerima  : ")
    daftar_email.append(tambah)
    f.write(tambah+'\n')
f.close()

sub=[]
while len(sub)==0:
    sub=input("Masukkan subject (wajib) : ")

isi=input("Masukkan pesan email     : ")

with_atch=input("Ada attachment ? (Y/N)   : ")
while (with_atch!="Y") and (with_atch!="N") :
    with_atch=input("Ada attachment ? (Y/N)   : ")

#Setup the MIME
msg = MIMEMultipart()  

if with_atch=="Y":
    atch=input("Attachment (1 file)      : ")
    print()
    filename = atch
    attachment = open(atch,"rb") 
    # instance of MIMEBase and named as p 
    p = MIMEBase('application', 'octet-stream') 
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
    # encode into base64 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    # attach the instance 'p' to instance 'msg' 
    msg.attach(p)

if with_atch=="N":
    print()

for x in daftar_email:
# storing the senders email address   
    msg['From'] = fromaddr 
# storing the receivers email address  
    msg['To'] = x 
# storing the subject  
    msg['Subject'] = sub
# string to store the body of the mail 
    body = isi
# attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
# creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
    s.starttls() 
# Authentication 
    s.login(fromaddr, pswd) 
# Converts the Multipart msg into a string 
    text = msg.as_string() 
# sending the mail 
    s.sendmail(fromaddr, x, text) 
# terminating the session 
    s.quit() 

print("Message succesfully sent")
print("---------------------------------------------------------")