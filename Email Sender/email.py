import smtplib

to = input("Enter the recivers email id : \n")

content = input("Enter the content to send : \n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Senderemail@gmail.com', 'Password')
    server.sendmail('Senderemail@gmail.com', to, content) 
    server.close() 

sendEmail(to, content)