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
    def export_data_by_type_and_month_and_year(connection, work_type, min_month, max_month, year):
        connection.cur.execute(
            "SELECT final.id, final.year, final.month, final.day, "
            "products.name, final.type, final.work, final.produce, final.data "
            "FROM final JOIN products ON final.id = products.id WHERE type=? AND ?<=month AND month<=? AND year=? ",
            (work_type, min_month, max_month, year,))
        data = connection.cur.fetchall()
        exporter(data, work_type, min_month, max_month, year)
        return data

    @staticmethod
    def export_ppm_data(connection, work_type, month):
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
