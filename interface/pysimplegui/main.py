import PySimpleGUI as sg
from util.settings import settings_runner
from application.commands import *
from interface.pysimplegui.add_expense_window import add_expense_window
from interface.pysimplegui.edit_expense_window import edit_expense_window


def main():
    # ------ Data for the table ------
    data = DatabaseActions.update_view()
    header_list = DatabaseActions.get_column_names()

    # ------ Table creation ------
    table = [[sg.Table(values=data,
                       headings=header_list,
                       justification='center',
                       num_rows=20,
                       key='-TABLE-',
                       enable_events=True)]]

    # ------ Tabs ------
    table_tab = [[sg.Button("Add expense", size=(15, 1)),
                  sg.Button("Remove", size=(10, 1)),
                  sg.Button("Edit", size=(10, 1)),
                  sg.T("Sort by:"),
                  sg.Combo(['name', 'date', 'category', 'value'], enable_events=True, key='-combo-filter-')],
                 [sg.Column(table)]]
    chart_tab = [[sg.T("Charts will be here")]]

    # ------ Tabs Layouts ------
    frame_layout = [[sg.TabGroup([[sg.Tab('Table', table_tab), sg.Tab('Chart', chart_tab)]])]]

    # ------ Final window Layout ------
    menu_def = [['&Menu', ['&Settings     Ctrl-S', 'E&xit']], ['Help', ['About']]]

    layout = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
              [sg.Frame('View', frame_layout)]]

    # ------ Create Window ------
    window = sg.Window("Expense tracker (beta)", layout)

    # ------ Event Loop ------
    while True:
        event, values = window.read()
        print(event, values)  # TESTING
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


if __name__ == '__main__':
    main()
