"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, datetime, timedelta


def print_days():
    onedaydelta = timedelta(days=1)

    today = datetime.now()
    yesterday = today - onedaydelta
    in30days = today + 30 * onedaydelta

    print('Yesterday was: ', datetime.strftime(yesterday, '%d.%m.%Y'))
    print('Today is: ', datetime.strftime(today, '%d.%m.%Y'))
    print('In 30 days will be: ', datetime.strftime(in30days, '%d.%m.%Y'))


def str_2_datetime(date_string):
    return repr(datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f'))


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
