import PySimpleGUI as sg
from util.settings import settings_runner
from util.db_handler import view_all
from application.commands import run


def main_window():
    data = view_all()[0]
    header_list = view_all()[1]
    menu_def = [['&Menu', ['&Settings     Ctrl-S', 'E&xit']], ['Help', ['About']]]
    table = [[sg.Table(values=data,
                       headings=header_list,
                       justification='center',
                       num_rows=20,
                       key='-TABLE-',
                       enable_events=True)]]
    table_tab = [[sg.Button("Add expense", size=(15, 1)),
                  sg.Button("Remove", size=(10, 1)),
                  sg.Button("Edit", size=(10, 1)),
                  sg.T("Sort by:"),
                  sg.Combo(['name', 'date', 'category', 'value'], enable_events=True, key='-combo-filter-')],
                 [sg.Column(table)]]
    chart_tab = [[sg.T("Charts will be here")]]
    frame_layout = [[sg.TabGroup([[sg.Tab('Table', table_tab), sg.Tab('Chart', chart_tab)]])]]
    layout = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
              [sg.Frame('View', frame_layout)]]
    window = sg.Window("Expense tracker (beta)", layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event == "Add expense":
            add_expense_window()
        elif event == "Remove":
            sg.popup_yes_no("Do you want to remove record XXX?")
        elif event == "Edit":
            edit_expense_window()
        elif event == '-combo-filter-':
            pass
        elif event == 'Settings     Ctrl-S':
            settings_runner()
        elif event == 'About':
            sg.Popup("Created by: Pawel Pruszynski\nE-mail: geopawel90@gmail.com\n", title='About')
        elif event == sg.WIN_CLOSED or event == 'Exit':
            break
    window.close()


def add_expense_window():
    col = [[sg.Text("Name", size=(10, 1)), sg.In(key='-NAME-')],
           [sg.Text("Date", size=(10, 1)), sg.In(key='-DATE-')],
           [sg.Text("Category", size=(10, 1)),
            sg.Combo(['restaurant', 'fuel', 'food'], key='-COMBO-CAT-ADD-')],
           [sg.Text("Value", size=(10, 1)), sg.In(key='-VALUE-')],
           [sg.Button("Add")]
           ]

    window = sg.Window("Add new expense", col)

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Add':
            run(event, values)
            sg.Popup("Expense added")

    window.close()


def edit_expense_window():
    col = [[sg.Text("Name", size=(10, 1)), sg.In(key='-NAME-')],
           [sg.Text("Date", size=(10, 1)), sg.In(key='-DATE-')],
           [sg.Text("Category", size=(10, 1)),
            sg.Combo(['restaurant', 'fuel', 'food'], enable_events=True, key='-combo-cat-edit-')],
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


main_window()
