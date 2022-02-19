import sys
import PySimpleGUI as sg
# 'Tape Player free icon image: Flaticon.com'. This cover has been designed using resources from Flaticon.com

# definiujemy wygląd aplikacji
app_layout = [
    [sg.Image(filename="tape-player.png")],
    [sg.Text("Sample text element")],
    [sg.Button("Sprawdź email")],
    [sg.Text("Another text element")],
    [sg.OK(), sg.Exit()],
]

window = sg.Window("Example layout", app_layout)
while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WIN_CLOSED or event == "Exit":
        print("Hard EXIT")
        break

# koniec programu
window.close()
print("End of application")
sys.exit(0)
