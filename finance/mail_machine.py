import smtplib
from cs50 import SQL
import base64

def notify(name, email):

    db = SQL("sqlite:///finance.db")
    adm = db.execute("SELECT * FROM adm;")

    sender = adm[0]['email']
    password = base64.b64decode(adm[0]['coded_pass']).decode("utf-8")

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(sender, password)

        subject='CASH OUT - DIGITAL BROKERS'
        body = f'Dear {name},\n\nyour holdings have been transfered to you.\n\nThanks for using Digital Brokers'
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(sender, f"{email}", msg)
