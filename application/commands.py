from infrastructure.database_handler import add_record

import uuid


class Command:
    def __init__(self, event, values):
        self.event = event
        self.values = values

    def create_object(self):
        uuid = 5
        name = self.values['-NAME-']
        date = self.values['-DATE-']
        category = self.values['-COMBO-CAT-ADD-']
        value = self.values['-VALUE-']
        return {'id': id, 'product': name, 'vendor_id': int(date), 'value': int(value)}


class Validator:
    pass


class AddExpenseCommand:
    pass


def run(event, value):
    obj = Command(event, value)
    obj_att = obj.create_object()
    add_record(obj_att)
    print(obj_att)
