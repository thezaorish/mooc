#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
import sys

from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    data = [[sheet.cell_value(r, col)
                for col in range(sheet.ncols)]
                    for r in range(sheet.nrows)]

    coast_row = sheet.col_values(1, start_rowx=1, end_rowx=sheet.nrows)
    sum = 0
    min = sys.float_info.max
    minidx = -1
    max = -sys.float_info.max
    maxidx = -1
    count = 0
    for num in coast_row:
        if isinstance(num, float):
            sum += num
            count += 1
            if min > num:
                min = num
                minidx = coast_row.index(num)
            if max < num:
                max = num
                maxidx = coast_row.index(num)
    
    data = {
            'maxtime': xlrd.xldate_as_tuple(sheet.cell_value(maxidx + 1, 0), 0),
            'maxvalue': max,
            'mintime': xlrd.xldate_as_tuple(sheet.cell_value(minidx + 1, 0), 0),
            'minvalue': min,
            'avgcoast': sum / count
    }
    return data


def test():
    # open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()