from sqlalchemy import create_engine, MetaData, Table, String, Column, Integer, Float, ForeignKey


def insert(table):
    if table == 'bills':
        return bills.insert().values(
            id=1,
            product='vacuum cleaner',
            vendor_id=1001,
            value=100.50
        )
    elif table == 'vendors':
        return vendors.insert().values(
            vendor_id=1002,
            vendor_name='Lidl'
        )
    else:
        print('Incorrect input')


def add_record(data):
    print(data)
    print(data['vendor_id'])
    engine = create_engine('sqlite:////sqlite/db/expenses.db')
    metadata = MetaData(engine)
    temp = Table('test2', metadata, autoload=True)
    ins = temp.insert().values(
        id=data['id'],
        product=data['product'],
        vendor_id=data['vendor_id'],
        value=data['value']
    )
    conn = engine.connect()
    conn.execute(ins)


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


main()
