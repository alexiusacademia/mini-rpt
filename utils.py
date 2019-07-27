import xlsxwriter


locations = {
    '001': 'BANCAL',
    '002': 'BANGAN',
    '003': 'BATONLAPOC',
    '004': 'BENEG',
    '005': 'CAPAYAWAN',
    '006': 'CARAEL',
    '007': 'DANACBUNGA',
    '009': 'MAMBOG',
    '011': 'PACO',
    '012': 'PANAN',
    '013': 'PAREL',
    '014': 'PAUDPOD',
    '016': 'PORAC AND BINOCLUTAN',
    '017': 'SAN ISIDRO',
    '018': 'SAN JUAN',
    '019': 'SAN MIGUEL',
    '020': 'SANTIAGO',
    '021': 'TAMPO',
    '022': 'TAUGTOG'
}


def write(obj, _row, file_name, td_num='', tp_name=''):
    wb = xlsxwriter.Workbook(file_name)
    ws = wb.add_worksheet('asa')

    # Formatting cells
    bold_format = wb.add_format({
        'bold': True
    })
    border_top = wb.add_format()
    border_top.set_top()

    border_bottom = wb.add_format()
    border_bottom.set_bottom()

    border_left = wb.add_format()
    border_left.set_left()

    border_right = wb.add_format()
    border_right.set_right()

    border_surround = wb.add_format()
    border_surround.set_top()
    border_surround.set_right()
    border_surround.set_bottom()
    border_surround.set_left()
    border_surround.set_bold()

    border_hat = wb.add_format()
    border_hat.set_top()
    border_hat.set_right()
    border_hat.set_left()

    border_boot = wb.add_format()
    border_boot.set_bottom()
    border_boot.set_left()
    border_boot.set_right()

    border_left_top = wb.add_format()
    border_left_top.set_left()
    border_left_top.set_top()

    border_right_top = wb.add_format()
    border_right_top.set_top()
    border_right_top.set_right()

    border_left_bottom = wb.add_format()
    border_left_bottom.set_left()
    border_left_bottom.set_bottom()

    border_right_bottom = wb.add_format()
    border_right_bottom.set_right()
    border_right_bottom.set_bottom()

    border_sides = wb.add_format()
    border_sides.set_left()
    border_sides.set_right()

    # Set column widths
    column_widths = [
        11.89, 29.89, 15.22, 12.11, 11.22, 9.89, 10.89, 10.56, 13.78
    ]
    for index, width in enumerate(column_widths):
        ws.set_column(index, index, width)

    for i in range(3):
        ws.write(_row, i, '', border_top)

    for index, av in enumerate(obj['assessed_values']):
        if index == 0:
            ws.write(index + _row, 3, av, border_hat)
        else:
            ws.write(index + _row, 3, av, border_sides)

    for index, tax_due in enumerate(obj['tax_dues']):
        if index == 0:
            ws.write(index + _row, 4, tax_due, border_hat)
        else:
            ws.write(index + _row, 4, tax_due, border_sides)

    for index, years_due in enumerate(obj['years_dues']):
        if index == 0:
            ws.write(index + _row, 5, years_due, border_hat)
        else:
            ws.write(index + _row, 5, years_due, border_sides)

    for index, taxes_due in enumerate(obj['taxes_dues']):
        if index == 0:
            ws.write(index + _row, 6, taxes_due, border_hat)
        else:
            ws.write(index + _row, 6, taxes_due, border_sides)

    for index, penalty in enumerate(obj['penalties']):
        if index == 0:
            ws.write(index + _row, 7, penalty, border_hat)
        else:
            ws.write(index + _row, 7, penalty, border_sides)

    for index, total in enumerate(obj['totals']):
        if index == 0:
            ws.write(index + _row, 8, total, border_hat)
        else:
            ws.write(index + _row, 8, total, border_sides)

    _num_rows = len(obj['totals'])
    ws.write(_num_rows + _row, 7, "BASIC", border_sides)
    ws.write(_num_rows + _row, 8, obj['basic'], border_hat)
    ws.write(_num_rows + 1 + _row, 7, "SEF", border_sides)
    ws.write(_num_rows + 1 + _row, 8, obj['sef'], border_sides)
    ws.write(_num_rows + 2 + _row, 7, "TOTAL", border_boot)
    ws.write(_num_rows + 2 + _row, 8, obj['total_tax'], border_surround)

    _total_rows = _num_rows + 3

    _assessed_values_rows = len(obj['assessed_values'])

    for i in range(_total_rows - _assessed_values_rows):
        ws.write(i + _row + _assessed_values_rows, 3, '', border_sides)
        ws.write(i + _row + _assessed_values_rows, 4, '', border_sides)

    for i in range(_num_rows, _total_rows):
        ws.write(i + _row, 5, '', border_sides)
        ws.write(i + _row, 6, '', border_sides)

    for i in range(7):
        ws.write(_total_rows + _row - 1, i, '', border_boot)

    # Draw left bottom corner borders
    ws.write(_num_rows + 2 + _row, 0, '', border_left_bottom)

    for i in range(3):
        for j in range(_num_rows + 3):
            if j == 0:
                ws.write(j, i, '', border_hat)
            elif j == _num_rows+2:
                ws.write(j, i, '', border_boot)
            else:
                ws.write(j, i, '', border_sides)

    # Draw left top corner borders
    ws.write(_row, 0, td_num, border_left_top)
    ws.write(_row, 1, tp_name, border_hat)

    # Get the td-number root
    td_root = td_num[0:3]
    if td_root in locations:
        ws.write(_row, 2, locations[td_root], border_hat)

    wb.close()