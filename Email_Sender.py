from  email.message import EmailMessage
import ssl
import smtplib

email_sender = 'hardikespana@gmail.com'
email_password = 'ilurtwfwlfck'

email_receiver = 'hello@gmail.com'

subject = "Don't Forget to Code"
body ="""
When you open this repo,Make sure you try it out!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
