class ReworkController:

    @staticmethod
    def fetch_all_reworks(connection, product_id):
        connection.cur.execute("SELECT rework.rework FROM rework WHERE productId=?", (product_id,))
        rows = connection.cur.fetchall()
        for index in range(len(rows)):
            rows[index] = rows[index][0]
        return rows

    @staticmethod
    def add_rework(connection, rework, product_id, severity, detection):
        connection.cur.execute("INSERT INTO rework VALUES (NULL,?,?,?,?)", (rework, product_id, severity, detection))
        connection.conn.commit()

    @staticmethod
    def fetch_rework_by_name(connection, product_id, rework_name):
        connection.cur.execute("SELECT id FROM rework WHERE productId=? AND rework=?", (product_id, rework_name,))
        rows = connection.cur.fetchone()
        return rows
