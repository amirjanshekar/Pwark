import sqlite3


class Connection:
    def __init__(self):
        self.conn = sqlite3.connect('Data/pwark.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name text)")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS years (id INTEGER PRIMARY KEY, year INTEGER)")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS wastages (id INTEGER PRIMARY KEY, wastage text, productId INTEGER,  "
            "severity INTEGER, detection INTEGER, FOREIGN KEY(productId) REFERENCES products(id) )")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS rework (id INTEGER PRIMARY KEY, rework text, productId INTEGER,  "
            "severity INTEGER, detection INTEGER, FOREIGN KEY(productId) REFERENCES products(id) )")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS final (id INTEGER PRIMARY KEY, year INTEGER, month INTEGER, "
            "day INTEGER, product INTEGER, type text, work text,workId INTEGER, produce INTEGER, data INTEGER, "
            "FOREIGN KEY(product) REFERENCES products(id) )")
        self.conn.commit()

    def __del__(self):
        self.conn.close()
