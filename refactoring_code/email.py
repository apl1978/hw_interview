import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
GMAIL_SMTP = config["MAIL"]["smtp"]
GMAIL_IMAP = config["MAIL"]["imap"]
PORT = config["MAIL"]["port"]
LOGIN = config["MAIL"]["login"]
PASSWORD = config["MAIL"]["password"]

subject = 'Subject'
recipients = ['vasya@email.com', 'petya@email.com']
message_text = 'Message'
header = None


class Email():

    def __init__(self, smtp, imap, port, login, password):
        self.smtp = smtp
        self.imap = imap
        self.port = port
        self.login = login
        self.password = password

    def send_message(self, recipients, subject, message_text):
        # send message
        message = MIMEMultipart()
        message['From'] = self.login
        message['To'] = ', '.join(recipients)
        message['Subject'] = subject
        message.attach(MIMEText(message_text))
        connect = smtplib.SMTP(self.smtp, self.port)
        # identify ourselves to smtp gmail client
        connect.ehlo()
        # secure our email with tls encryption
        connect.starttls()
        # re-identify ourselves as an encrypted connection
        connect.ehlo()
        connect.login(self.login, self.password)
        connect.sendmail(self.login, recipients, message.as_string())
        connect.quit()
        # send end

    def receive_messages(self, mailbox, criterion):
        # recieve
        mail = imaplib.IMAP4_SSL(self.imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select(mailbox)
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message
        # end recieve


if __name__ == '__main__':
    email = Email(GMAIL_SMTP, GMAIL_IMAP, PORT, LOGIN, PASSWORD)
    email.send_message(recipients, subject, message_text)
    criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
    email_message = email.receive_messages('inbox', criterion)
