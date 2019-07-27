def get_table(assessed_values=[], current_year: int = 2019, last_payment=1984):
    _tax_dues = []

    for index, assessed_value in enumerate(assessed_values):
        _tax_dues.append(assessed_value * 0.01)

    _old_rows = 3

    if 1984 <= last_payment <= 1992:
        _old_rows = 3
    elif 1993 <= last_payment <= 2001:
        _old_rows = 2
    elif 2002 <= last_payment <= 2012:
        _old_rows = 1
    else:
        _old_rows = 0

    _remaining_years_qty = 0
    if last_payment <= 2012:
        _remaining_years_qty = current_year - 2013
    else:
        _remaining_years_qty = current_year - last_payment

    _num_rows = _old_rows + _remaining_years_qty

    _taxes_dues = []
    _years_dues = []
    _penalties = []
    _totals = []

    if _old_rows == 3:
        for i in range(_old_rows):
            _taxes_due = 0
            _years_due = ''

            if i == 0:
                _first_due_start = str(last_payment + 1)
                _first_due_end = '1993'

                _taxes_due = _tax_dues[i] * (1993 - last_payment)
                _years_due = _first_due_start + '-' + _first_due_end if _first_due_start != _first_due_end \
                    else _first_due_start
            elif i == 1:
                _taxes_due = _tax_dues[i] * 9
                _years_due = '1994-2002'
            else:
                _taxes_due = _tax_dues[i] * 11
                _years_due = '2003-2013'

            _penalty = round(0.72 * _taxes_due, 2)
            _total = _taxes_due + _penalty

            _taxes_dues.append(_taxes_due)
            _years_dues.append(_years_due)
            _penalties.append(_penalty)
            _totals.append(_total)

    elif _old_rows == 2:
        for i in range(_old_rows):
            _taxes_due = 0
            _years_due = ''

            if i == 0:
                _first_due_start = str(last_payment + 1)
                _first_due_end = '2002'

                _taxes_due = _tax_dues[i] * (2002 - last_payment)
                _years_due = _first_due_start + '-' + _first_due_end if _first_due_start != _first_due_end \
                    else _first_due_start
            else:
                _taxes_due = _tax_dues[i] * 11
                _years_due = '2003-2013'

            _penalty = round(0.72 * _taxes_due, 2)
            _total = _taxes_due + _penalty

            _taxes_dues.append(_taxes_due)
            _years_dues.append(_years_due)
            _penalties.append(_penalty)
            _totals.append(_total)

    elif _old_rows == 1:
        _taxes_due = 0
        _years_due = ''

        _first_due_start = str(last_payment + 1)
        _first_due_end = '2013'

        _taxes_due = _tax_dues[0] * (2013 - last_payment)
        _years_due = _first_due_start + '-' + _first_due_end if _first_due_start != _first_due_end \
            else _first_due_start

        _penalty = round(0.72 * _taxes_due, 2)
        _total = _taxes_due + _penalty

        _taxes_dues.append(_taxes_due)
        _years_dues.append(_years_due)
        _penalties.append(_penalty)
        _totals.append(_total)

    for i in range(_old_rows, _num_rows):
        _taxes_due = 0
        _years_due = ''
        _base_year = 2014
        _penalty = 0
        if last_payment <= 2013:
            _base_year = 2014
        else:
            _base_year = last_payment + 1

        _year = i - _old_rows + _base_year

        _years_due = str(_year)
        if _year == 2014:
            _td1 = _tax_dues[len(_tax_dues) - 2]
            _td2 = _tax_dues[len(_tax_dues) - 1]
            _taxes_due = _td1 + ((_td2 - _td1) * 0.35)
        elif _year == 2015 or _year == 2016:
            _td1 = _tax_dues[len(_tax_dues) - 2]
            _td2 = _tax_dues[len(_tax_dues) - 1]
            _taxes_due = _td1 + ((_td2 - _td1) * 0.7)
        else:
            _taxes_due = _tax_dues[len(_tax_dues) - 1]

        if _year <= 2017:
            _penalty = round(0.72 * _taxes_due, 2)
        elif _year == 2018: # 2018
            _penalty = round(0.48 * _taxes_due, 2)
        elif _year == 2019: # 2019
            _penalty = round(0.24 * _taxes_due, 2)

        _taxes_dues.append(_taxes_due)
        _years_dues.append(_years_due)
        _penalties.append(_penalty)
        _totals.append(_taxes_due + _penalty)

    _basic = 0

    for _total in _totals:
        _basic += _total

    _sef = _basic

    _total_tax = _basic + _sef

    obj = {'assessed_values': assessed_values, 'tax_dues': _tax_dues, 'years_dues': _years_dues,
           'taxes_dues': _taxes_dues, 'penalties': _penalties, 'totals': _totals, 'basic': _basic, 'sef': _sef,
           'total_tax': _total_tax}

    return obj
