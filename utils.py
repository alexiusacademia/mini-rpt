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


def write(obj, _row, file_name, td_num='', tp_name='', wb=None, ws=None):
    # Formatting cells
    bold_format = wb.add_format({
        'bold': True
    })
    border_top = wb.add_format()
    border_top.set_top()
    border_top.set_font_name('Times New Roman')

    border_bottom = wb.add_format()
    border_bottom.set_bottom()
    border_bottom.set_font_name('Times New Roman')

    border_left = wb.add_format()
    border_left.set_left()
    border_left.set_font_name('Times New Roman')

    border_right = wb.add_format()
    border_right.set_right()
    border_right.set_font_name('Times New Roman')

    border_surround = wb.add_format()
    border_surround.set_top()
    border_surround.set_right()
    border_surround.set_bottom()
    border_surround.set_left()
    border_surround.set_bold()
    border_surround.set_num_format('#,##0.00')
    border_surround.set_font_name('Times New Roman')

    border_hat = wb.add_format()
    border_hat.set_top()
    border_hat.set_right()
    border_hat.set_left()
    border_hat.set_align('top')
    border_hat.set_font_name('Times New Roman')

    border_hat_center = wb.add_format()
    border_hat_center.set_top()
    border_hat_center.set_right()
    border_hat_center.set_left()
    border_hat_center.set_align('top')
    border_hat_center.set_align('center')
    border_hat_center.set_font_name('Times New Roman')

    border_hat_numeric = wb.add_format()
    border_hat_numeric.set_top()
    border_hat_numeric.set_right()
    border_hat_numeric.set_left()
    border_hat_numeric.set_num_format('#,##0.00')
    border_hat_numeric.set_align('top')
    border_hat_numeric.set_font_name('Times New Roman')

    border_hat_wrap = wb.add_format()
    border_hat_wrap.set_left()
    border_hat_wrap.set_top()
    border_hat_wrap.set_right()
    border_hat_wrap.set_text_wrap()
    border_hat_wrap.set_font_name('Times New Roman')

    border_boot = wb.add_format()
    border_boot.set_bottom()
    border_boot.set_left()
    border_boot.set_right()
    border_boot.set_font_name('Times New Roman')

    border_left_top = wb.add_format()
    border_left_top.set_left()
    border_left_top.set_top()
    border_left_top.set_font_name('Times New Roman')

    border_right_top = wb.add_format()
    border_right_top.set_top()
    border_right_top.set_right()
    border_right_top.set_font_name('Times New Roman')

    border_left_bottom = wb.add_format()
    border_left_bottom.set_left()
    border_left_bottom.set_bottom()
    border_left_bottom.set_font_name('Times New Roman')

    border_right_bottom = wb.add_format()
    border_right_bottom.set_right()
    border_right_bottom.set_bottom()
    border_right_bottom.set_font_name('Times New Roman')

    border_sides = wb.add_format()
    border_sides.set_left()
    border_sides.set_right()
    border_sides.set_font_name('Times New Roman')

    border_sides_center = wb.add_format()
    border_sides_center.set_left()
    border_sides_center.set_right()
    border_sides_center.set_align('center')
    border_sides_center.set_font_name('Times New Roman')

    border_sides_numeric = wb.add_format()
    border_sides_numeric.set_left()
    border_sides_numeric.set_right()
    border_sides_numeric.set_num_format('#,##0.00')
    border_sides_numeric.set_font_name('Times New Roman')

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
            ws.write(index + _row, 3, round(av, 2), border_hat_numeric)
        else:
            ws.write(index + _row, 3, round(av, 2), border_sides_numeric)

    for index, tax_due in enumerate(obj['tax_dues']):
        if index == 0:
            ws.write(index + _row, 4, round(tax_due, 2), border_hat_numeric)
        else:
            ws.write(index + _row, 4, round(tax_due, 2), border_sides_numeric)

    for index, years_due in enumerate(obj['years_dues']):
        if index == 0:
            ws.write(index + _row, 5, years_due, border_hat_center)
        else:
            ws.write(index + _row, 5, years_due, border_sides_center)

    for index, taxes_due in enumerate(obj['taxes_dues']):
        if index == 0:
            ws.write(index + _row, 6, round(taxes_due, 2), border_hat_numeric)
        else:
            ws.write(index + _row, 6, round(taxes_due, 2), border_sides_numeric)

    for index, penalty in enumerate(obj['penalties']):
        if index == 0:
            ws.write(index + _row, 7, round(penalty, 2), border_hat_numeric)
        else:
            ws.write(index + _row, 7, round(penalty, 2), border_sides_numeric)

    for index, total in enumerate(obj['totals']):
        if index == 0:
            ws.write(index + _row, 8, round(total, 2), border_hat_numeric)
        else:
            ws.write(index + _row, 8, round(total, 2), border_sides_numeric)

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
                ws.write(j + _row, i, '', border_hat)
            elif j == _num_rows+2:
                ws.write(j + _row, i, '', border_boot)
            else:
                ws.write(j + _row, i, '', border_sides)

    # Draw left top corner borders
    ws.write(_row, 0, td_num, border_hat)
    ws.write(_row, 1, tp_name, border_hat_wrap)

    # Get the td-number root
    td_root = td_num[0:3]
    if td_root in locations:
        ws.write(_row, 2, locations[td_root], border_hat)
