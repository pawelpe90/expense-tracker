import sqlite3


def add_record():
    conn = sqlite3.connect(r"C:\sqlite\db\expenses.db")
    cur = conn.cursor()
    cur.execute("insert into test (product,store_name,bill_value)"
                "values ('stamples', 'post office', 5)")
    conn.commit()
    conn.close()


def view_all():
    conn = sqlite3.connect(r"C:\sqlite\db\default.db")
    cur = conn.cursor()
    cur.execute("select * from data")
    data = cur.fetchall()
    names = list(map(lambda x: x[0], cur.description))
    conn.commit()
    conn.close()
    return data, names
