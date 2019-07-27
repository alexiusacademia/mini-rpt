from templates import *
from utils import *

from xlsx import *


if __name__ == '__main__':
    filename = 'list_of_delinquent.xlsx'
    file_name = 'output.xlsx'
    wb = Workbook(filename)

    rows = []

    for sheet in wb:
        for row, cells in sheet.rowsIter():
            row_obj = {}
            assessed_values = []
            for index, cell in enumerate(cells):
                if index == 0:
                    row_obj['td_number'] = cell.value
                elif index == 1:
                    if cell.value:
                        row_obj['name'] = cell.value.upper()
                    else:
                        row_obj['name'] = ''
                elif index == 3 or index == 4 or index == 5 or index == 6:
                    if cell.value != '':
                        assessed_values.append(float(cell.value))
                elif index == 7:
                    row_obj['last_payment'] = int(cell.value)
            row_obj['assessed_values'] = assessed_values

            rows.append(row_obj)

    wb = xlsxwriter.Workbook(file_name)
    ws = wb.add_worksheet('asa')

    _current_row = 0    # Current row in spreadsheet
    for index, row in enumerate(rows):
        if row['last_payment'] <= 1992:
            _row_height = 12
        elif row['last_payment'] <= 2001:
            _row_height = 11
        elif row['last_payment'] <= 2012:
            _row_height = 10
        else:
            _row_height = 10 - (int(row['last_payment']) + 1 - 2013)

        obj = get_table(assessed_values=row['assessed_values'], current_year=2019, last_payment=row['last_payment'])
        write(obj, _current_row, td_num=row['td_number'], tp_name=row['name'], file_name=file_name, wb=wb, ws=ws)
        _current_row += _row_height + 2

    wb.close()

    print('Process complete.')
