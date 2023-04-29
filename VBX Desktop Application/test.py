import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define email parameters
sender_email = 'akshaypiranavb@gmail.com'
sender_password = 'AKSHAYPIRANAV@1234'
recipient_email = 'akshaypiranavb@gmail.com'
subject = 'Test Email'
body = 'This is a test email sent using Python.'

# Create a multipart message and set headers
message = MIMEMultipart()
message['From'] = "akshaypiranavb@gmail.com"
message['To'] = "akshaypiranavb@gmail.com"
message['Subject'] = "HI BRO"

# Add body to email
message.attach(MIMEText(body, 'plain'))

# Create SMTP session and send the email
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email, sender_password)
    smtp.sendmail(sender_email, recipient_email, message.as_string())
    print('Email sent successfully')