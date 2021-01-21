from infrastructure.database_handler import MightyActions


class AddExpense:
    def __init__(self):
        pass

    @staticmethod
    def load_expense(expense_object):
        item = MightyActions(expense_object)
        item.add_record()


class EditExpense:
    def __init__(self):
        pass
