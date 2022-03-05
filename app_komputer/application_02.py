import sys
import requests
import PySimpleGUI as sg
# 'Tape Player free icon image: Flaticon.com'. This cover has been designed using resources from Flaticon.com

password = {
    "adasiek": "qwerty1234",
}

sendmail = {
    "mailfrom": "nikt@polska.pl",
    "mailto": None,
    "mailok": False,
}

"""
/test_email/{email_to} - endpoint do testowania emaila
"""


def api_connect_test(api_address="http://127.0.0.1:8000"):
    try:
        requests.get(api_address)
    except:
        sg.popup_auto_close("ERROR connecting to API!", auto_close_duration=3)
        sys.exit(2)


def api_email_test(email_to_check="none@domain.com", api_address="http://127.0.0.1:8000"):
    api_check = f"{api_address}/test_email/{email_to_check}"
    print(f"TEST: {api_check} ")
    api_result = requests.get(api_check)
    if api_result.status_code == 202:
        sendmail["mailto"] = email_to_check
        sendmail["mailok"] = True
        return True
    return False

# testujemy dostęp do API
api_connect_test()

# definiujemy wygląd aplikacji
app_layout = [
    [sg.Column([
        [sg.Image("tape-player.png", tooltip=f"This is an icon")]],
        justification="center")],
    [sg.Text("Please enter an email address for verify:")],
    [sg.InputText("email@domain.com")],
    [sg.Column([
        [sg.Button("Sprawdź email")]],
        justification="center")],
    [sg.Text("Od razu coś tam")],
    [sg.InputText("")],
    [sg.OK(), sg.Exit()],
]

window = sg.Window("Example layout", app_layout)
while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED or event == "Exit":
        print("Hard EXIT")
        break

    if event == "Sprawdź email":
        print("Sprawdzamy email")
        check_email = values[1]
        if not check_email:
            sg.popup_auto_close(
                "There is no data in email field!!!!",
                title="ERROR",
                auto_close_duration=2,
            )
        ret_code = api_email_test(check_email)
        if ret_code:
            sg.popup_auto_close("Mail_spec OK", auto_close_duration=2)
        else:
            sg.popup_auto_close("Mail_spec ERROR", auto_close_duration=3)

# koniec programu
window.close()
print("End of application")
sys.exit(0)
