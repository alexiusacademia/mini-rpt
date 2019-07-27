from templates import *
from utils import *


if __name__ == '__main__':
    obj = get_table(226800,
                    current_year=2019,
                    last_payment=2018)

    write(obj, 0, 'output.xlsx', td_num="003-0457A", tp_name='ACADEMIA, ALEXIUS')
