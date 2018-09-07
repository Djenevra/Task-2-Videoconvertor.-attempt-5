import smtplib
#smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
#smtpObj.login('fortestsonly23@gmail.com','for123tests')


sender = "fortestsonly23@gmail.com"
recipient = "fortestsonly23@gmail.com"
password = "for123tests"
subject = "ghjkl;kjhgfhjk"
text = "wqertyuiouytretyui"
smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.ehlo()
smtp_server.starttls()
smtp_server.login(sender,password)
message = "Subject: {}\n\n{}".format(subject, text)
smtp_server.sendmail(sender, recipient, message)
smtp_server.quit()
