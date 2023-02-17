import csv
import os


def write_csv(file_path, header, row):
    with open(file_path, 'a', encoding='utf8', newline='\n') as file:
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize(file_path) == 0:
            csv_writer.writeheader()
        csv_writer.writerow(row)
    print('data savved succesfully')