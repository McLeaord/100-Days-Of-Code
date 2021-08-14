import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("*****@gmail.com","password")
server.sendmail("*****@gmail.com","*****@gmail.com","HELLO")

server.quit()