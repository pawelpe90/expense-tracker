from sqlalchemy import create_engine, MetaData, Table, select


class Actions:
    PATH = r'sqlite:////sqlite/db/expenses.db'

    @staticmethod
    def update_view():
        engine = create_engine(Actions.PATH)
        conn = engine.connect()
        metadata = MetaData(engine)
        items = Table('items', metadata, autoload=True)
        vends = Table('vendors', metadata, autoload=True)
        merge = items.join(vends, items.c.vendor_id == vends.c.vendor_id)
        ins = select([items.c.id,
                      items.c.description,
                      vends.c.vendor_name,
                      items.c.category,
                      items.c.value,
                      items.c.date,
                      items.c.created]).select_from(merge)
        r = conn.execute(ins)
        return r.fetchall(), r.keys()

    @staticmethod
    def get_vendors():
        engine = create_engine(Actions.PATH)
        metadata = MetaData(engine)
        vends = Table('vendors', metadata, autoload=True)
        s = vends.select()
        conn = engine.connect()
        r = conn.execute(s)
        return r.fetchall()


class MightyActions:
    PATH = r'sqlite:////sqlite/db/expenses.db'

    def __init__(self, data):
        self.data = data

    def add_record(self):
        engine = create_engine(Actions.PATH)
        metadata = MetaData(engine)
        items = Table('items', metadata, autoload=True)
        ins = items.insert().values(
            uuid=self.data['uuid'],
            description=self.data['description'],
            date=self.data['date'],
            category=self.data['category'],
            vendor_id=self.data['vendor'],
            value=self.data['value']
        )
        conn = engine.connect()
        conn.execute(ins)
