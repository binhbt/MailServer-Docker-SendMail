import smtplib

client = smtplib.SMTP('localhost')

fromaddr = 'admin@kidssy.com'
toaddrs = 'thanhbinh.gd@gmail.com'
msg = 'Hello'

client.sendmail(fromaddr, toaddrs, msg)
client.quit()
