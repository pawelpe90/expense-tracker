import PySimpleGUI as sg
"""
    Demonstration of MENUS!
    How do menus work?  Like buttons is how.
    Check out the variable menu_def for a hint on how to 
    define menus
"""


def second_window():

    layout = [[sg.Text('The second form is small \nHere to show that opening a window using a window works')],
              [sg.OK()]]

    window = sg.Window('Second Form', layout)
    event, values = window.read()
    window.close()


def test_menus():

    sg.theme('LightGreen')
    sg.set_options(element_padding=(0, 0))

    # ------ Menu Definition ------ #
    menu_def = [['&File', ['&Open     Ctrl-O', '&Save       Ctrl-S', '&Properties', 'E&xit']],
                ['&Edit', ['&Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['&Toolbar', ['---', 'Command &1', 'Command &2',
                              '---', 'Command &3', 'Command &4']],
                ['&Help', '&About...'], ]

    right_click_menu = ['Unused', ['Right', '!&Click', '&Menu', 'E&xit', 'Properties']]

    # ------ GUI Defintion ------ #
    layout = [
        [sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
        [sg.Text('Right click me for a right click menu example')],
        [sg.Output(size=(60, 20))],
        [sg.ButtonMenu('ButtonMenu',  right_click_menu, key='-BMENU-'), sg.Button('Plain Button')],
    ]

    window = sg.Window("Windows-like program",
                       layout,
                       default_element_size=(12, 1),
                       default_button_element_size=(12, 1),
                       right_click_menu=right_click_menu)

    # ------ Loop & Process button menu choices ------ #
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        print(event, values)
        # ------ Process menu choices ------ #
        if event == 'About...':
            window.disappear()
            sg.popup('About this program', 'Version 1.0',
                     'PySimpleGUI Version', sg.version,  grab_anywhere=True)
            window.reappear()
        elif event == 'Open':
            filename = sg.popup_get_file('file to open', no_window=True)
            print(filename)
        elif event == 'Properties':
            second_window()

    window.close()


# test_menus()

# inspector = inspect(engine)
#
# for table_name in inspector.get_table_names():
#     print(table_name)
#     for column in inspector.get_columns(table_name):
#         print("Column: %s" % column['name'])

# for t in metadata.tables:
#     print(metadata.tables[t])
#
# print(vendors.columns)


def demo():
    import PySimpleGUI as sg
    import random
    import string

    """
        Basic use of the Table Element
    """

    sg.theme('Dark Red')

    # ------ Some functions to help generate data for the table ------
    def word():
        return ''.join(random.choice(string.ascii_lowercase) for i in range(10))

    def number(max_val=1000):
        return random.randint(0, max_val)

    def make_table(num_rows, num_cols):
        data = [[j for j in range(num_cols)] for i in range(num_rows)]
        data[0] = [word() for __ in range(num_cols)]
        for i in range(1, num_rows):
            data[i] = [word(), *[number() for i in range(num_cols - 1)]]
        return data

    # ------ Make the Table Data ------
    data = make_table(num_rows=15, num_cols=6)
    headings = [str(data[0][x]) + '     ..' for x in range(len(data[0]))]

    # ------ Window Layout ------
    print(data[1:][:])
    layout = [[sg.Table(values=data[1:][:], headings=headings, max_col_width=25,
                        # background_color='light blue',
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification='right',
                        num_rows=20,
                        alternating_row_color='lightyellow',
                        key='-TABLE-',
                        row_height=35,
                        tooltip='This is a table')],
              [sg.Button('Read'), sg.Button('Double'), sg.Button('Change Colors')],
              [sg.Text('Read = read which rows are selected')],
              [sg.Text('Double = double the amount of data in the table')],
              [sg.Text('Change Colors = Changes the colors of rows 8 and 9')]]

    # ------ Create Window ------
    window = sg.Window('The Table Element', layout,
                       # font='Helvetica 25',
                       )

    # ------ Event Loop ------
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        if event == 'Double':
            for i in range(len(data)):
                data.append(data[i])
            window['-TABLE-'].update(values=data)
        elif event == 'Change Colors':
            window['-TABLE-'].update(row_colors=((8, 'white', 'red'), (9, 'green')))

    window.close()

demo()