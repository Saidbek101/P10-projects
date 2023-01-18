from datetime import datetime

def error_log(file: str, error: str) -> None:
    try:
        with open(file, 'x') as file:
            date = datetime.now().strftime('%d-%m-%Y %X')
            file.write(f'{error} DATE: {date}\n')

    except FileExistsError:
        with open(file, 'a') as file:
            date = datetime.now().strftime('%d-%m-%Y %X')
            file.write(f'{error} DATE: {date}\n')