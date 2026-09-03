'''
                                                 smtplib module
                                                 ----------------
                                                 ----------------
- this module is used to send a mail without opening or using mail, or outlook.
- this is done by running only the python code
- and here by using port 587 (mention correct port number, or server will not respond correctly)

#to send mail

import smtplib

sender_mail = 'saitrishankb9@gmail.com'
sender_app_password = 'vqrb vrus znch ugng'
receiver_mail = 'satyasaishivakoviri2004@gmail.com'

message = """
Subject: Python Testing


Hello,

This mail is from Bannuuu, sent using python ra huka


Regards,
Sai Trishank
"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_mail, sender_app_password)
for i in range(10):
    server.sendmail(
        sender_mail,
        receiver_mail,
        message
)

server.quit()
print("Email sent successfully")

----------------------------------------------------------------------------------------------------------------------
# to send mail with subject, to and from

import smtplib
from email.message import EmailMessage

sender_mail = "saitrishankb9@gmail.com"
sender_app_password = "vqrb vrus znch ugng"

receiver_mail = "satyasaishivakoviri2004@gmail.com"

msg = EmailMessage()

msg['From'] = sender_mail
msg['To'] = receiver_mail
msg['Subject'] = 'Python Testing mail'

msg.set_content("""
Hello,

This mail is from Bannuuu, sent using python ra huka

Regards,
Sai Trishank
""")

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(sender_mail, sender_app_password)

server.send_message(msg)

server.quit()

print("Email sent successfully")
---------------------------------------------------------------------------------------------------------------------------------------------
'''

import smtplib
from email.message import EmailMessage

sender_mail = "saitrishankb9@gmail.com"
sender_app_password = "vqrb vrus znch ugng"

receiver_mail = "bannusai899@gmail.com"

msg = EmailMessage()

msg['From'] = sender_mail
msg['To'] = receiver_mail
msg['Subject'] = 'Python Testing mail'

msg.set_content("""
Hello,

This mail is from Bannuuu, sent using python ra huka

Regards,
Sai Trishank
""")

with open("day12.py", "rb") as file:
    file_content = file.read()
    
msg.add_attachment(
        file_content,
        maintype = 'application',
        subtype = 'py',
        filename = 'day12.py'
    )
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_mail, sender_app_password)
    server.send_message(msg)

print("Email sent successfully")
