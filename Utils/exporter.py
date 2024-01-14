import csv
import openpyxl
from Controllers.products_controller import ProductsController
from Controllers.rework_controller import ReworkController
from Controllers.wastage_controller import WastageController


def exporter(data, work_type):
    for item in data:
        srcfile = openpyxl.load_workbook('./Forms/{}.xlsx'.format(work_type), read_only=False, keep_vba=True)
        sheet_name = srcfile.get_sheet_by_name('1')
        sheet_name['C2'] = item[4]
        sheet_name['E2'] = f'{item[1]}/{item[2]}/{item[3]} تاریخ: '
        for m in range(5, 14):
            if sheet_name[f'E{m}'].value is None and sheet_name[f'B{m}'].value is None:
                sheet_name[f'E{m}'] = item[8]
                sheet_name[f'B{m}'] = item[6]
                break

        srcfile.save('./Output/{}.xlsm'.format(item[4]))


def ppm_exporter(connection, data, work_type, month='', year=''):
    with open(f'./Output/ppm_export_{work_type}_{year}_{month}.csv', 'w', encoding="utf-8-sig", newline='') as out:
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
