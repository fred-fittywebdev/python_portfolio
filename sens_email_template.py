import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "portfolio.py.fred@gmail.com"
password = "xdrrkirgjdzmifny"
receiver = "loulou.fg@gmail.com"

context = ssl.create_default_context()

message = """\
Subject: Contact from the portfolio.
Hello!
How are you today?
Ciao !
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

