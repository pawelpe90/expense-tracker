from infrastructure.database_handler import Actions


class DatabaseActions:
    def __init__(self):
        pass

    @staticmethod
    def update_view():
        obj = Actions()
        view = [list(i) for i in obj.update_view()[0]]
        for item in view:
            item[5] = str(item[5])
            item[6] = str(item[6])
        return view

    @staticmethod
    def get_column_names():
        obj = Actions()
        names = obj.update_view()[1]
        return names

    @staticmethod
    def get_vendor_names():
        cont = []
        for ven in Actions.get_vendors():
            cont.append(ven[1])
        cont.sort()
        return cont


print(DatabaseActions.update_view())
