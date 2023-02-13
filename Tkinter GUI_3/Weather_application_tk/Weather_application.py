import json
import os
import requests
import tkinter as tk
from tkinter import ttk, Tk, Frame, X, END
from dotenv import load_dotenv
from datetime import datetime
from itertools import cycle

from functions import error_log

load_dotenv()


class WeatherManager:
    API_KEY = os.environ.get('API_KEY')
    FILE = 'Tkinter GUI_3/weather.json'

    def __init__(self, city):
        self.city = city

    @staticmethod
    def convert_to_datetime(date_str):
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")

    def save_info(self):
        url = f"https://api.tomorrow.io/v4/weather/forecast?" \
              f"location={self.city}&apikey={self.API_KEY}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        try:
            with open(self.FILE, "w") as file:
                if os.path.getsize(self.FILE) == 0:
                    if response.status_code == 200:
                        json.dump(json.loads(response.text), file)
        except FileNotFoundError as e:
            error_log('error.log', e)

    def get_data(self):
        file_json = None

        try:
            with open(self.FILE) as file:
                if os.path.getsize(self.FILE) == 0:
                    self.save_info()
                file_json = json.load(file)
        except FileNotFoundError as e:
            error_log('error.log', e)

        return file_json

    def get_timelines(self):
        res = self.get_data()
        return res.get("timelines")

    def get_daily_data(self):
        timelines = self.get_timelines()
        if timelines:
            return timelines.get("daily")

    def get_hourly_data(self):
        timelines = self.get_timelines()
        if timelines:
            return timelines.get("hourly")

    def get_day_hours_temperature_with_time(self, day_date):
        hourly_data = self.get_hourly_data()
        data = []

        for hour_data in hourly_data:
            time = hour_data.get("time")
            if self.convert_to_datetime(time).date() == day_date.date():
                data.append({
                    "time": self.convert_to_datetime(time).strftime("%H:%M"),
                    "temperature": hour_data["values"].get("temperature")
                })
        return data

    def get_daily_temperature(self):
        data = []
        for day in self.get_daily_data():
            day_values = day.get("values")
            average_temperature = None
            if day_values:
                average_temperature = day_values.get("temperatureAvg")
            day_date = datetime.strptime(day.get("time"), "%Y-%m-%dT%H:%M:%SZ")
            data.append({
                "day": day_date.strftime("%Y.%m.%d"),
                "average_temperature": average_temperature,
                "hours": self.get_day_hours_temperature_with_time(day_date)
            })

        return data


def clear_window():
    for widget in root.grid_slaves()[6:]:

        if int(widget.grid_info()["row"]) > 3:
            widget.grid_forget()


def refresh():
    clear_window()

    dates = weather.get_daily_temperature()
    for i in range(len(dates)):
        tk.Label(root, foreground='green', text=dates[i].get('day')).grid(row=3, column=i, sticky='w')

        hours = dates[i].get('hours')
        for j in range(len(hours)):
            text = f'{hours[j].get("time")} ~ {hours[j].get("temperature")}°C'
            tk.Label(root, foreground='blue', text=text).grid(row=j + 4, column=i, sticky='w')


weather = WeatherManager("Tashkent")

cities = ["Tashkent", "Moscow", "Italy"]

root = Tk()
root.title("Weather")
root.geometry("400x400")

country_combo = ttk.Combobox(root, values=[i.title() for i in cities], width=10)
country_combo.current(0)
country_combo.grid(row=1, column=0)
country_label = tk.Label(root, text='Select country')
country_label.grid(row=0, column=0)

refresh_btn = tk.Button(root, text="Select", command=refresh)
refresh_btn.grid(row=1, column=1)

root.mainloop()