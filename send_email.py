import smtplib, ssl


def send_emails(message):
    host = "smtp.gmail.com"
    port = 465
    username = "kanadaaryan9@gmail.com"
    password = "mttl froj xvsy bzew"

    receiver = "kanadaaryan9@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port,context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)