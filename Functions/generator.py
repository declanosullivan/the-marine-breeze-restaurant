import datetime
from tables.models import Tables, TableAvail


def check_availability(table_no, table_start, table_end):
    avail_list = []
    tables_list = TableAvail.objects.filter(table_no=table_no)
    for table in tables_list:
        if table_no.table_start > table_end or table_no.table_end < table_start:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
