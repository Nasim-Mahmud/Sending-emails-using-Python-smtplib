import smtplib

my_email = ""
my_pass = ""

test_email = ""

with smtplib.SMTP() as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(from_addr=my_email,
                        to_addrs=test_email,
                        msg="Subject:This is a subject\n\n This is the actual message")
