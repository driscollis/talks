import PySimpleGUI as sg

layout = [[sg.Button("OK")],
          [sg.Button("OK 2")],
          [sg.Button("OK 3")],
          [sg.Button("OK 4")],
          [sg.Button("OK 5")]]

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