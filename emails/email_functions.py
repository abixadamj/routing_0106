import smtplib, ssl
from email.mime.text import MIMEText


def mail_report(mail_to: str, mail_from: str, data: str) -> bool:
    ip = "mail.abix.info.pl"
    port = 465  # For SSL
    login = "kielce-2022@abix.info.pl"
    password = "_kh7sVSybnd!W8D"
    ####

    text_type = 'plain'  # or 'html'
    msg = MIMEText(data, text_type, 'utf-8')
    msg['Subject'] = "Pydantic Mail report - fastAPI APP"
    msg['From'] = mail_from
    #
    msg['To'] = mail_to

    try:
        # Create a secure SSL context
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(ip, port, context=context) as server:
            server.login(login, password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
        return (True, "Test mail SUCCESS")
    except Exception as e:
        return (False, e)


if __name__ == "__main__":
    print(f"to jest tylko uruchomienie testowe: {__name__}")
    mail_ok, report = mail_report("abix.edukacja@gmail.com", "kielce-2022@abix.info.pl", "TESTOWY MAIL")
    if mail_ok:
        print(report)
    else:
        print(f"Test mail failed - {report}")
else:
    print(f"Importujemy moduł: {__name__}")