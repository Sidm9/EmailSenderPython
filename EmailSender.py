import smtplib
import config

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = "Subject : {}\n\n{}".format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.test,  message)
        server.quit()
        print("Success : Email Sent!")
    except:
        print("Email Failed to send.")


subject = "Test Subject"
msg = "Hel-lo De-lo!!"

send_email(subject, msg)
