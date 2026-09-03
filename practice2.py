
'''#Calculator

def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1 / num2
def powers(num1, num2):
    return num1 ** num2


a = [23, 45, 53, 63, 73, 83, 43]
for i in range(0, len(a)):
    
    print(int(a[i]))
    print(float(a[i]))
    print(str(a[i]))
----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------
07 aug DSA
---------

rows = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(col):
        value = int(input(f'Enter value at position ({i},{j}): '))
        row.append(value)
    matrix.append(row)
print("The matrix is: ")
for row in matrix:
    print(row)

-------------------------------------------------------------------------------------------------------------------------------------------------
matrix = [
               [1,2,3],
               [3,5,6],
               [7,8,9]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j])
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
import smtplib
from email.message import EmailMessage

sender_mail = 'saitrishankb9@gmail.com'
sender_app_password = 'vqrb vrus znch ugng'
receiver_mail = 'garikapatitejachowdary@gmail.com'

msg = EmailMessage()

msg['From'] = sender_mail
msg['To'] = receiver_mail
msg['Subject'] = "Python Testing Mail"

msg.set_content("""
Good afternoon Sir,

Im trishank.....

""")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_mail, sender_app_password)
server.send_message(msg)
server.quit()
print("Email Sent")
