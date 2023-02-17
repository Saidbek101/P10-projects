import csv
import os

from tg_bot.TG_bots_part1.Weather_bot.weather import get_daily_temperature

STUDENTS = 'weather_app/students.csv'


def write_to_csv(student):
    with open(STUDENTS, "a+", newline="\n") as f:
        header = ["chat_id", "fullname"]
        csv_writer = csv.DictWriter(f, header)
        if os.path.getsize(STUDENTS) == 0:
            csv_writer.writeheader()
        csv_writer.writerow(student.get_attrs_for_csv_writer())
    print("Student add successfully.")


def is_exist_chat_id(chat_id):
    with open(STUDENTS) as f:
        csv_reader = csv.DictReader(f)
        return chat_id in [int(row.get("chat_id")) for row in csv_reader]


def get_weather_days():
    temperatures = get_daily_temperature()
    return [day_temp.get("day") for day_temp in temperatures]