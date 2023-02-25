import csv
from Controllers.rework_controller import ReworkController
from Controllers.wastage_controller import WastageController
from Controllers.products_controller import ProductsController


def exporter(data, work_type, min_month='', max_month='', year=''):
    with open(f'export_{work_type}_{year}_{min_month} to {max_month}.csv', 'w', encoding="utf-8-sig",
              newline='') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['row', 'year', 'month', 'day', 'product', 'type', 'work', 'produce', 'amount'])
        for item in data:
            csv_out.writerow(item)


def ppm_exporter(connection, data, work_type, month='', year=''):
    with open(f'ppm_export_{work_type}_{year}_{month}.csv', 'w', encoding="utf-8-sig", newline='') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['row', 'product', 'type', 'work', 'month', 'ppm', 'rpn', 'grade'])
        c = 1
        for item in data:
            for item2 in data[item]:
                product_name = ProductsController.fetch_product_by_id(connection, item)[0]
                if work_type == 'rework':
                    work_name = ReworkController.fetch_rework_by_id(connection, item, item2)[0]
                else:
                    work_name = WastageController.fetch_wastage_by_id(connection, item, item2)[0]
                csv_out.writerow(
                    (c, product_name, work_type, work_name, month, data[item][item2]['ppm'], data[item][item2]['rpn'],
                     data[item][item2]['grade']))
                c += 1
