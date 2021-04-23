# import dependencies

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email
import email.mime.application
from django.utils.html import strip_tags

# create message
msg = MIMEMultipart('alternative')
msg['Subject'] = "Test Mail : ThePythonDjango.Com"
msg['From'] = "sender-email-id@gmail.com"
msg['To'] = "receivers-email-id@gmail.com"

# create body
html_text = '<div style="border:1px solid black">This is your message body in HTML format.</div>'
plain_text = strip_tags(html_text)

# Create the body of the message (a plain-text and an HTML version).
# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(plain_text, 'plain')
part2 = MIMEText(html_text, 'html')

# Attach image if any

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
host = "smtp.gmail.com"
port = 587
mail = smtplib.SMTP(host, port, timeout=60)
mail.ehlo()
mail.starttls()

# Add recepiens, cc or bcc if any
recepient = [msg["To"]]

# username and password of gmail id which will be used to send email
username = "your-user-name"
password = "*****"

# login using credentials
mail.login(username, password)

# send email
mail.sendmail(msg["From"], recepient, msg.as_string())
mail.quit()

print("\nSent\n")
