import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
email_from = 'artur.aloyan20@gmail.com'  # Sender's email address
email_password = 'xbspiedatamisryv'  # Sender's email password or an app-specific password
email_to = 'artur.aloyan20@gmail.com'  # Recipient's email address
smtp_server = 'smtp.gmail.com'
smtp_port = 587
subject = 'Project 2'
message_body = 'Tuyn'  # The message body

msg = MIMEMultipart()
msg['From'] = email_from
msg['To'] = email_to
msg['Subject'] = subject
msg.attach(MIMEText(message_body, 'plain'))

try:
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()  # Start TLS encryption
    smtp.login(email_from, email_password)  # Use your Gmail password or app-specific password
    smtp.sendmail(email_from, email_to, msg.as_string())
    print('Email sent successfully.')
except (smtplib.SMTPException, socket.error) as e:
    print(f'An error occurred: {e}')
finally:
    smtp.quit()
