import uuid
import re
from application.exceptions import *


class Validator:
    def __init__(self, event, values):
        self.event = event
        self.values = values
        self.item = []

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
