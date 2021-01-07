import PySimpleGUI as sg


def edit_expense():
    col = [[sg.Text("Name", size=(10, 1)), sg.In(key='-NAME-')],
           [sg.Text("Date", size=(10, 1)), sg.In(key='-DATE-')],
           [sg.Text("Category", size=(10, 1)),
            sg.Combo(['restaurant', 'fuel', 'food'], enable_events=True, key='-combo-cat-')],
           [sg.Text("Value", size=(10, 1)), sg.In(key='-VAL-')],
           [sg.Button("Save")]
           ]

    window = sg.Window("Edit existing expense", col)

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Save':
            print(values['-NAME-'])
            sg.Popup("Expense saved!")

    window.close()
