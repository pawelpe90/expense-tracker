import datetime
from infrastructure.database_handler import Actions


class FormatSetter:
    def __init__(self, obj):
        self.obj = obj

    def date_setter(self):
        date_raw = self.obj['date']
        drs = date_raw.split("/")
        return datetime.date(int(drs[2]), int(drs[1]), int(drs[0]))

    def vendor_name_to_id(self):
        for code, vendor in Actions.get_vendors():
            if vendor == self.obj['vendor']:
                return code

    def format_setter(self):

        return {'uuid': str(self.obj['uuid']),
                'description': self.obj['description'],
                'date': FormatSetter.date_setter(self),
                'category': self.obj['category'],
                'vendor': FormatSetter.vendor_name_to_id(self),
                'value': float(self.obj['value'])}
