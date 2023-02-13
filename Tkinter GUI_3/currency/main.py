import tkinter as tk
import json
import requests
import os
from dotenv import load_dotenv

from tkinter import ttk, Tk, Frame, X, END
from function import error_log

load_dotenv()

API_KEY = 'gKOeS2ZI3wK4zTeGcKeZ8dgBp9psidFl1ntV2cAR'
print(API_KEY)
url = f"https://api.freecurrencyapi.com/v1/latest"

try:
    res = requests.get(
        url=url,
        params={'apikey': API_KEY}
    )

    with open("converter.json", "w") as file:
        json.dump(json.loads(res.text), file)

    currencies = json.loads(res.text).get('data')

except (ConnectionRefusedError, ConnectionAbortedError, ConnectionError) as e:
    error_log('error.log', e)

    try:
        with open("converter.json") as file:
            currencies = json.load(file).get('data')

    except FileNotFoundError as e:
        error_log('error.log', e)

root = Tk()
root.title("Converter")
root.geometry('400x150')
root['bg'] = 'LightBlue'


def converter():
    clear()

    sum_ = round(currencies.get(from_.get()), 2) * round(currencies.get(to_.get()), 2)
    result = (round(currencies.get(to_.get()), 2) * sum_) * float(currency_input.get('1.0', END))
    output.insert("1.0", f'{result:.2f}')


def clear():
    output.delete("1.0", END)


header_frame = Frame(root)
header_frame.pack(fill=X)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

from_ = ttk.Combobox(header_frame, values=[i for i in currencies])
from_.current(1)
from_.grid(padx=0, pady=25)

to_ = ttk.Combobox(header_frame, values=[i for i in currencies])
to_.current(2)
to_.grid(column=2, row=0)

from_currency_label = tk.Label(root, text="From")
from_currency_label.place(x=45, y=0)

to_currency = tk.Label(root, text="To")
to_currency.place(x=265, y=0)

currency_input = tk.Text(root, width=25, height=8)
currency_input.place(x=25, y=55, width=138, height=40)

output = tk.Text(root, width=25, height=8)
output.place(x=240, y=55, width=138, height=40)

convert_button = tk.Button(root, text="CONVERT", command=converter)
convert_button['bg'] = 'lightgreen'
convert_button.place(x=168, y=100)

root.mainloop()
