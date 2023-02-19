class WastageController:

    @staticmethod
    def fetch_all_wastage(connection):
        connection.cur.execute("SELECT wastages.wastage FROM wastages")
        rows = connection.cur.fetchall()
        return rows

    @staticmethod
    def add_wastage(connection, wastage, product_id, severity, detection):
        connection.cur.execute("INSERT INTO wastages VALUES (NULL,?,?,?,?)", (wastage, product_id, severity, detection))
        connection.conn.commit()
