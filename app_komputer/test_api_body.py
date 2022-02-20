# 5-6 marca - dorobimy testowanie fastAPI
import requests


sendmail = {
    "mailfrom": "kielce-2022@abix.info.pl",
    "mailto": "abix.edukacja@gmail.com",
    "mailok": True,
    "mailbody": "testowy mail - TEST"
}


def test_send_mail(api_address="http://127.0.0.1:8000"):
    api_send = f"{api_address}/send_email_body/"
    mail_params = {
        "mail_from": sendmail["mailfrom"],
        "mail_to": sendmail["mailto"],
        "mail_body": sendmail["mailbody"]
    }
    auth_params = {
        "auth_id": "adasiek",  # tego nie robimy na produkcji !!!!
        "auth_password": "qwerty1234",  # tego nie robimy na produkcji !!!!
    }
    api_result = requests.post(api_send, json=mail_params, headers=auth_params)
    return api_result


if __name__ == "__main__":
    res = test_send_mail()
    print(res)
    print(res.text)
