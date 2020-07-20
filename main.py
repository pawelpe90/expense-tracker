import PySimpleGUI as sg
from util.settings import settings_runner

layout = [[sg.Button("Add expense")],
          [sg.Button("Check balance")],
          [sg.Button("Settings")],
          [sg.Button("Exit")]]

window = sg.Window("Expense tracker (beta)", layout, margins=(100, 100))

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Settings":
        settings_runner()

window.close()