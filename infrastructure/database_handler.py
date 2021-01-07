from sqlalchemy import create_engine, MetaData, Table, String, Column, Integer, Float, ForeignKey


class Actions:
    def __init__(self):
        pass

    @staticmethod
    def update_view():
        engine = create_engine('sqlite:////sqlite/db/expenses.db')
        conn = engine.connect()
        metadata = MetaData(engine)
        items = Table('items', metadata, autoload=True)
        ins = items.select()
        r = conn.execute(ins)
        return r.fetchall()

    @staticmethod
    def get_column_names():
        engine = create_engine('sqlite:////sqlite/db/expenses.db')
        conn = engine.connect()
        metadata = MetaData(engine)
        items = Table('items', metadata, autoload=True)
        ins = items.select()
        r = conn.execute(ins)
        return r.keys()


def add_record(data):
    # print(data)
    engine = create_engine('sqlite:////sqlite/db/expenses.db')
    metadata = MetaData(engine)
    items = Table('items', metadata, autoload=True)
    ins = items.insert().values(
        uuid=data['uuid'],
        description=data['description'],
        date=data['date'],
        category=data['category'],
        vendor_id=data['vendor'],
        value=data['value']
    )
    conn = engine.connect()
    conn.execute(ins)


def get_vendors():
    engine = create_engine('sqlite:////sqlite/db/expenses.db')
    metadata = MetaData(engine)
    vends = Table('vendors', metadata, autoload=True)
    s = vends.select()
    conn = engine.connect()
    r = conn.execute(s)
    return r.fetchall()


def main():
    global bills, vendors

    engine = create_engine('sqlite:////sqlite/db/expenses.db')
    metadata = MetaData()

    # CREATE NEW TABLES

    bills = Table('test2', metadata,
                  Column('id', Integer(), primary_key=True),
                  Column('product', String(100)),
                  Column('vendor_id', Integer(), ForeignKey('vendors.vendor_id')),
                  Column('value', Float(), nullable=False))
    vendors = Table('vendors', metadata,
                    Column('vendor_id', Integer(), primary_key=True),
                    Column('vendor_name', String(100), nullable=False))

    # metadata.create_all(engine)

    # CREATE NEW TABLES

    conn = engine.connect()
    # conn.execute(insert('bills'))
    # s = bills.select()
    # str(s)
    # r = conn.execute(s)
    # r.fetchall()

    test1 = Table('vendors', metadata, autoload=True)
    s = test1.select()
    r = conn.execute(s)
    print(r.fetchall())


# main()
