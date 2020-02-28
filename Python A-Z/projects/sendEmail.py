import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()

email['from'] = 'Nirmal Silwal'
email['to'] = 'email id here'
email['subject'] = 'You won 1,00,00,000 dollars'

# email.set_content('I am a python master')

email.set_content(html.substitute({'name':'tintin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email id here','password here')
    smtp.send_message(email)
    print('all good')