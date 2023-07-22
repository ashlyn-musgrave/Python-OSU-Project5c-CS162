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
        with open('sat.json', 'r') as f:
            self._data = json.load(f)['data']

    def save_as_csv(self, dbns):
        """This method takes as a parameter a list of DBNs (district bureau numbers) and saves a
        CSV file that looks like this, but with only the rows that correspond to the DBNs in the
        list"""
        sat_list = []
        for data in self._data:
            if data[8] in dbns:
                sat_list.append(data)

        with open('output.csv', 'w+') as outfile:
            header = [str(i) for i in range(len(sat_list[3]))]
            outfile.write
            for row in sat_list:
                sat_info = []
                for item in row:
                    if ',' in str(item):
                        sat_info.append("\"" + item + "\"")
                    else:
                        sat_info.append(str(item))
                outfile.write(','.join(sat_info))
                outfile.write('\n')
        outfile.close()

