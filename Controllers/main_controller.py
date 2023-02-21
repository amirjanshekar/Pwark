import csv


class MainController:

    @staticmethod
    def add_main(connection, data):
        connection.cur.execute("INSERT INTO main VALUES (NULL,?,?,?,?,?,?,?,?)",
                               (data['year'], data['month'], data['day'], data['product'], data['type'], data['work'],
                                data['produce'], data['data']))
        connection.conn.commit()

    @staticmethod
    def export_data_by_type(connection, work_type):
        connection.cur.execute("SELECT * FROM main WHERE type=?", (work_type,))
        rows = connection.cur.fetchall()
        with open(f'export_{work_type}.csv', 'a') as out:
            csv_out = csv.writer(out)
            csv_out.writerow(['row', 'year', 'month', 'day', 'product', 'type', 'work', 'produce', 'amount'])
            for row in rows:
                csv_out.writerow(row)
