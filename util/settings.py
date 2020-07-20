import PySimpleGUI as sg


def settings_runner():
    layout = [[sg.Text('Set up database connection')],
              [sg.Text('Db path'), sg.In(size=(25, 1), enable_events=True, key='-path-'), sg.FileBrowse()],
              [sg.Button('Save'), sg.Exit()]]

    window = sg.Window('Settings', layout)

    while True:
        event, values = window.read()
        if event == 'Save':
            sg.popup('You entered', values['-path-'])
        print(event, values)  # for the purpose of testing
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

    window.close()
