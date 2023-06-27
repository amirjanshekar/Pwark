class YearsController:

    def __init__(self):
        pass

    @staticmethod
    def fetch_all_years(connection):
        connection.cur.execute("SELECT * FROM years")
        rows = connection.cur.fetchall()
        return [{'id': row[0], 'year':row[1]} for row in rows]
