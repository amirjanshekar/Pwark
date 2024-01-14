from Utils.exporter import exporter, ppm_exporter
from Utils.ppm_calculator import ppm_calculator


class FinalController:

    def __init__(self):
        pass

    @staticmethod
    def add_final(connection, data):
        connection.cur.execute("INSERT INTO final VALUES (NULL,?,?,?,?,?,?,?,?,?)",
                               (data['year'], data['month'], data['day'], data['product'], data['type'], data['work'],
                                data['workId'], data['produce'], data['data']))
        connection.conn.commit()

    @staticmethod
    def fetch_all_data(connection):
        connection.cur.execute("SELECT * FROM final")
        rows = connection.cur.fetchall()
        print(rows)
        for index in range(len(rows)):
            rows[index] = rows[index][0]
        return rows

    @staticmethod
    def fetch_data(connection, year, month, day, work_type, product):
        connection.cur.execute("SELECT final.id, products.name, final.work FROM final JOIN products ON "
                               "final.id = products.id WHERE year=? AND month=? AND day=? AND type=? "
                               "AND product=?", (year, month, day, work_type, product,))
        rows = connection.cur.fetchall()
        return rows

    @staticmethod
    def fetch_data_by_type(connection, year, month, day, work_type):
        connection.cur.execute("SELECT final.id, products.name, final.work FROM final JOIN products ON "
                               "final.id = products.id WHERE year=? AND month=? AND day=? AND type=? "
                               , (year, month, day, work_type,))
        rows = connection.cur.fetchall()
        # for index in range(len(rows)):
        #     rows[index] = rows[index][0] + ',' +  ""
        return rows

    @staticmethod
    def export_data_by_type(connection, work_type):
        connection.cur.execute(
            "SELECT final.id, final.year, final.month, final.day, "
            "products.name, final.type, final.work, final.produce, final.data "
            "FROM final JOIN products ON final.id = products.id WHERE type=? ",
            (work_type,))
        rows = connection.cur.fetchall()

        exporter(rows, work_type)

        return rows

    @staticmethod
    def export_formatted_data(connection, work_type, month):
        connection.cur.execute(
            "SELECT final.id, final.year, final.month, final.day, "
            "products.name, final.type, final.work, final.workId, final.produce, final.data, final.product "
            "FROM final JOIN products ON final.id = products.id WHERE type=? AND month<? AND year=1401 ",
            (work_type, month,))
        data = connection.cur.fetchall()

        connection.cur.execute(
            "SELECT final.id, final.year, final.month, final.day, "
            "products.name, final.type, final.work,final.workId, final.produce, final.data, final.product "
            "FROM final JOIN products ON final.id = products.id WHERE type=? AND month>=? AND year=1400 ",
            (work_type, month,))
        data2 = connection.cur.fetchall()

        all_data = data + data2
        final_data = ppm_calculator(connection, work_type, all_data)

        ppm_exporter(connection, final_data, work_type, month, 1401)
        return data
