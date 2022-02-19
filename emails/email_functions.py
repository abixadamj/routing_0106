import smtplib, ssl
from email.mime.text import MIMEText


def mail_report(mail_to: str, mail_from: str, data: str) -> bool:
    ip = "SMTP_mail_server_name"
    port = 465  # For SSL
    login = ""
    password = ""
    ####

    text_type = 'plain'  # or 'html'
    msg = MIMEText(data, text_type, 'utf-8')
    msg['Subject'] = "Mail report - fastAPI APP"
    msg['From'] = mail_from
    #
    msg['To'] = mail_to

    try:
        # Create a secure SSL context
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(ip, port, context=context) as server:
            server.login(login, password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
        return True
    except:
        return False
