import smtplib

my_email = "tmailone01@gmail.com"
my_pass = "b&H24fs}Pf"

test_email = "tmailtwo02@yahoo.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_pass)
    connection.sendmail(from_addr=my_email,
                        to_addrs=test_email,
                        msg="Subject:This is a subject\n\n This is the actual message")

