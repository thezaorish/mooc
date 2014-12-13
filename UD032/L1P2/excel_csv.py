# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.

__author__ = 'zaorish'

import xlrd
import os
import csv
import sys
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = [[sheet.cell_value(r, col)
                for col in range(sheet.ncols)]
                    for r in range(sheet.nrows)]

    data_to_write = []
    headers_of_interest = sheet.row_values(0, start_colx=1, end_colx=sheet.ncols - 1)
    for region in headers_of_interest:
        row = []
        column = sheet.col_values(headers_of_interest.index(region) + 1, start_rowx=1, end_rowx=sheet.nrows)
        max, maxidx = extract_min(column)
        date = xlrd.xldate_as_tuple(sheet.cell_value(maxidx, 0), 0)
        row.append(region)
        row.append(date[0])
        row.append(date[1])
        row.append(date[2])
        row.append(date[3])
        row.append(max)
        data_to_write.append(row)

    return data_to_write


def extract_min(values):
    max = -sys.float_info.max
    maxidx = -1

    for num in values:
        if isinstance(num, float):
            if max < num:
                max = num
                maxidx = values.index(num)

    return (max, maxidx + 1) # +1 because of the 0-indexed

def save_file(data, filename):
    header = ['Station', 'Year', 'Month', 'Day', 'Hour', 'Max Load']
    with open(filename, 'wb') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter='|',  quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(header)
        for row in data:
            csv_writer.writerow(row)


def test():
    # open_zip(datafile) this is uncommented in the actual submission
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)


if __name__ == "__main__":
    test()