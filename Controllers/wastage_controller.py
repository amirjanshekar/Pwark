class WastageController:

    @staticmethod
    def fetch_all_wastage(connection, product_id):
        connection.cur.execute("SELECT wastages.wastage FROM wastages WHERE productId=?", (product_id,))
        rows = connection.cur.fetchall()
        for index in range(len(rows)):
            rows[index] = rows[index][0]
        return rows

    @staticmethod
    def add_wastage(connection, wastage, product_id, severity, detection):
        connection.cur.execute("INSERT INTO wastages VALUES (NULL,?,?,?,?)", (wastage, product_id, severity, detection))
        connection.conn.commit()

    @staticmethod
    def fetch_wastage_by_name(connection, product_id, wastage_name):
        connection.cur.execute("SELECT id FROM wastages WHERE productId=? AND wastage=?", (product_id, wastage_name,))
        rows = connection.cur.fetchone()
        return rows
