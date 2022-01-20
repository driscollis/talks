import PySimpleGUI as sg

left_column = [
    [
        sg.Text("Select Folder"),
        sg.Input(size=(25, 1), enable_events=True, key="-FNAME-"),
        sg.FolderBrowse()
    ]
]

right_column = [
    [
        sg.Button("Btn 1"),
        sg.Button("Btn 2"),
        sg.Button("Btn 3"),
    ],
    [
        sg.Button("Btn 4"),
        sg.Button("Btn 5"),
        sg.Button("Btn 6"),
    ]
]

layout = [
    [
        sg.Column(left_column),
        sg.VSeparator(),
        sg.Col(right_column)
    ]
]

window = sg.Window("Column Demo", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break