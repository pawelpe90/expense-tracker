import PySimpleGUI as sg
from application.commands import *


def add_expense_window():
    col = [[sg.Text("Description", size=(15, 1)), sg.In(key='-DESCR-')],
           [sg.Text("Date dd/mm/yyyy", size=(15, 1)), sg.In(key='-DATE-')],
           [sg.Text("Category", size=(15, 1)),
            sg.Combo(['restaurant', 'fuel', 'food'], key='-COMBO-CAT-ADD-')],
           [sg.Text("Vendor", size=(15, 1)),
            sg.Combo(get_vendor_names(), key='-COMBO-VEN-ADD-')],
           [sg.Text("Value", size=(15, 1)), sg.In(key='-VALUE-')],
           [sg.Button("Add")]
           ]

    window = sg.Window("Add new expense", col)

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Add':
            try:
                content = Validator(event, values)
                obj = content.create_expense_object()
                Validator.validate_object(obj)
                format_obj = FormatSetter(obj)
                AddExpense.load_expense(format_obj.format_setter())
                sg.Popup("Expense added")
            except DescriptionTooLong:
                sg.Popup("Incorrect format in field: description", title="Incorrect data format")
            except IncorrectDateFormat:
                sg.Popup("Incorrect year format. Year should have at least 4 digits and be higher that 1990",
                         title="Incorrect data format")
            except IncorrectCategoryFormat:
                sg.Popup("Category should consist of up to 50 letters")
            except ValueError:
                sg.Popup("Value field should consist of digits only", title="Incorrect data format")
            except ValueEqualsZero:
                sg.Popup("Value should be greater than 0", title="Incorrect data format")

    window.close()
