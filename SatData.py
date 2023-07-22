# Author: Ashlyn Musgrave
# GitHub Username: ashlyn-musgrave
# Date: 7/21/2023
# Description: This program reads a JSON file containing data on 2010 SAT results for New York
# City and writes the data to a text file in CSV format

import json

class SatData:
    """This class reads a JSON file containing data on 2010 SAT results for New York City and
    writes the data to a text file in CSV format"""

    def __init__(self):
        """This method reads the file and stores it in a data method"""
        with open('sat.json', 'r') as file:
            self.data = json.load(file)

    def save_as_csv(self, dbn_list):
        """This method takes as a parameter a list of DBNs (district bureau numbers) and saves a
        CSV file that looks like this, but with only the rows that correspond to the DBNs in the
        list"""
        rows = []
        headers = ['DBN', 'School Name', 'Number of Test Takers', 'Critical Reading Mean', 'Mathematics Mean', 'Writing Mean']

        for school_data in self.data:
            if school_data['DBN'] in dbn_list:
                row = []
                for header in headers:
                    value = school_data[header]
                    if ',' in value:
                        value = '"' + value + '"'
                    row.append(value)
                rows.append(row)

        rows = sorted(rows, key=lambda x: x[0])

        with open('output.csv', 'w') as f:
            f.write(','.join(headers) + '\n')

            for row in rows:
                f.write(','.join(row) + '\n')
