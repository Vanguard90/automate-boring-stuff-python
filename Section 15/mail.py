import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo()

conn.starttls()

print(type(conn))