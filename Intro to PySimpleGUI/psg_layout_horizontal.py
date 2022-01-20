import PySimpleGUI as sg

# Horizontal layout
layout = [[sg.Button(f"OK {num}") for num in range(1, 6)]]

# Create the window
window = sg.Window("Demo", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()