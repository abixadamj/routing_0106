import PySimpleGUI as sg

# sg.popup("Hej - to ja!")

sg.popup(
    "Welcome to our script.",
    "We have some informations to you",
    title="Test TEXT Window",
    button_type=sg.POPUP_BUTTONS_YES_NO,
    custom_text=("Text A", "Text B"),
    line_width=150,
)

sg.popup_auto_close(
    "So, if you wait 4 seconds ...",
    title="Some title",
    auto_close_duration=4,
)