import csv
import os


def write_csv(student):
    with open('students.csv', 'a+', newline='\n') as file:
        header = ['chad_id', 'fullname']
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize('students.csv') == 0:
            csv_writer.writeheader()
        csv_writer.writerow(student.get_attrs_for_csv_writer())

    print('Successfully')
