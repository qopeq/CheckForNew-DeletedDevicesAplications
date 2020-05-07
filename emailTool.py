import smtplib


def sendEmail(messgage, time):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.connect("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login("rycerzinternetow@gmail.com", "!!!!!!!!!!!!!!!!!!!!!!!!!!")
    except:
        print("Fail with conntection!")
    msg1 = """From: Mua <rycerzinternetow@gmail.com>
To: Mua <rycerzinternetow@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

"""
    msg2 = messgage.__str__()

    msg3 = time

    msg4 = """
"""
    msg = msg1 + msg2 + msg3 + msg4


    try:
        server.sendmail("rycerzinternetow@gmail.com", "rycerzinternetow@gmail.com", msg)
    except:
        print("Fail with sending!")