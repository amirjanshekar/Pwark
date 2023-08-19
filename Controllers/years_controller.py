class YearsController:

    def __init__(self):
        pass

    @staticmethod
    def fetch_all_years(connection):
        connection.cur.execute("SELECT * FROM years")
        rows = connection.cur.fetchall()
        return [{'id': row[0], 'year': row[1]} for row in rows]

    @staticmethod
    def add_year(connection, year):
        connection.cur.execute("INSERT INTO years VALUES  (NULL, ?) ", [year])
        connection.conn.commit()

    @staticmethod
    def remove_year(connection, year_id):
        connection.cur.execute("DELETE FROM years WHERE id=?", (year_id,))
        connection.conn.commit()

