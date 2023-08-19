import csv
import shutil
import xlsxwriter
import openpyxl


def exporter(data, work_type, min_month='', max_month='', year=''):
    for item in data:
        srcfile = openpyxl.load_workbook('./Forms/{}.xlsx'.format(work_type), read_only=False, keep_vba=True)
        sheet_name = srcfile.get_sheet_by_name('1')
        sheet_name['C2'] = item[4]
        for m in range(5, 14):
            if sheet_name[f'E{m}'].value is None and sheet_name[f'B{m}'].value is None:
                sheet_name[f'E{m}'] = item[8]
                sheet_name[f'B{m}'] = item[6]
                break

        srcfile.save('./Output/{}.xlsm'.format(item[4]))


def ppm_exporter(connection, data, work_type, month='', year=''):
    print(data)
    shutil.copy2(r'Forms/wastages.xlsx', r'test_ppm_export_{}_{}_{}.xlsx'.format(work_type, year, month))
    work_book = xlsxwriter.Workbook('test_ppm_export_{}_{}_{}.xlsx'.format(work_type, year, month))
    work_book.get_worksheet_by_name('')
