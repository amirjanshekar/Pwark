import csv
import shutil
import xlsxwriter
import openpyxl


def exporter(data, work_type, min_month='', max_month='', year=''):
    with open(f'export_{work_type}_{year}_{min_month} to {max_month}.csv', 'w', encoding="utf-8-sig",
              newline='') as out:
        cells = []
        for j in range(4, 14):
            for i in ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']:
                cells.append(f'{i}{j}')
        csv_out = csv.writer(out)
        csv_out.writerow(['row', 'year', 'month', 'day', 'product', 'type', 'work', 'produce', 'amount'])
        for item in data:
            srcfile = openpyxl.load_workbook('./Forms/{}.xlsx'.format(work_type), read_only=False, keep_vba=True)
            sheet_name = srcfile.get_sheet_by_name('1')
            sheet_name['E2'] = item[4]
            for m in cells:
                if sheet_name[f'{i}{j}'].value is None:
                    sheet_name[f'{m}'] = item[8]
                    break
                else:
                    break

            srcfile.save('./Output/{}.xlsm'.format(item[4]))
            csv_out.writerow(item)


def ppm_exporter(connection, data, work_type, month='', year=''):
    print(data)
    shutil.copy2(r'Forms/wastages.xlsx', r'test_ppm_export_{}_{}_{}.xlsx'.format(work_type, year, month))
    work_book = xlsxwriter.Workbook('test_ppm_export_{}_{}_{}.xlsx'.format(work_type, year, month))
    work_book.get_worksheet_by_name('')
