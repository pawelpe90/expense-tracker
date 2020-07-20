import sqlite3


def add_record():
    conn = sqlite3.connect(r"C:\sqlite\db\expenses.db")
    cur = conn.cursor()
    cur.execute("insert into test (product,store_name,bill_value)"
                "values ('stamples', 'post office', 5)")
    conn.commit()
    conn.close()


add_record()
