from infrastructure.database_handler import *
from application.exceptions import *
import uuid
import datetime
import re


class Validator:
    def __init__(self, event, values):
        self.event = event
        self.values = values

    def create_expense_object(self):
        _uuid = uuid.uuid4()
        description = self.values['-DESCR-']
        date = self.values['-DATE-']
        category = self.values['-COMBO-CAT-ADD-']
        vendor = self.values['-COMBO-VEN-ADD-']
        value = self.values['-VALUE-']

        return {'uuid': _uuid,
                'description': description,
                'date': date,
                'category': category,
                'vendor': vendor,
                'value': value}

    @staticmethod
    def validate_object(expense_object):
        category_pattern = '^\w{0,50}$'
        date_pattern = '^\d{1,2}\/\d{1,2}\/(19|20)\d{2}$'
        vendor_pattern = '^[A-Za-z]{0,100}$'

        if len(expense_object['description']) > 50:
            raise DescriptionTooLong
        elif re.findall(date_pattern, expense_object['date']) == []:
            raise IncorrectDateFormat
        elif re.findall(category_pattern, expense_object['category']) == []:
            raise IncorrectCategoryFormat
        elif re.findall(vendor_pattern, expense_object['vendor']) == []:
            raise IncorrectVendorFormat
        elif int(expense_object['value']):
            pass
        elif int(expense_object['value']) == 0:
            raise ValueEqualsZero


class FormatSetter:
    def __init__(self, obj):
        self.obj = obj

    def date_setter(self):
        date_raw = self.obj['date']
        drs = date_raw.split("/")
        return datetime.date(int(drs[2]), int(drs[1]), int(drs[0]))

    def vendor_name_to_id(self):
        v = self.obj['vendor']
        if v == 'Lidl':
            return 1001
        elif v == 'Biedra':
            return 1002
        else:
            return 1000

    def format_setter(self):

        return {'uuid': str(self.obj['uuid']),
                'description': self.obj['description'],
                'date': FormatSetter.date_setter(self),
                'category': self.obj['category'],
                'vendor': FormatSetter.vendor_name_to_id(self),
                'value': float(self.obj['value'])}


class AddExpense(Validator):
    @staticmethod
    def load_expense(expense_object):
        add_record(expense_object)


class EditExpense(Validator):
    pass


class DatabaseActions:
    def __init__(self):
        pass

    @staticmethod
    def update_view():
        obj = Actions()
        view = [list(i) for i in obj.update_view()]
        for item in view:
            item[6] = str(item[6])
            item[7] = str(item[7])
        return view

    @staticmethod
    def get_column_names():
        obj = Actions()
        names = obj.get_column_names()
        return names


def get_vendor_names():
    cont = []
    for ven in get_vendors():
        cont.append(ven[1])
    cont.sort()
    return cont


# print(get_vendor_names())
# DatabaseActions.get_column_names()
DatabaseActions.update_view()
