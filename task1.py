#Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
#
#Вимоги до завдання:
#
#Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
#Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
#У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
#Для роботи з датами слід використовувати модуль datetime Python.

from datetime import datetime as dt, timedelta as td
from typing import Final

DATE_FORMAT: Final = '%Y-%m-%d'

def get_days_from_today(date):
    try:
        date_to_check = dt.strptime(date, DATE_FORMAT)
        date_difference = dt.today() - date_to_check
        return date_difference.days
    except:
        print(f"Invalid date: {date}")    



#Checks
DAYS_DIFFERENCE: Final = 2
date_in_future = dt.today() + td(days=DAYS_DIFFERENCE)
print(get_days_from_today(date_in_future.strftime(DATE_FORMAT)))

assert get_days_from_today(date_in_future.strftime(DATE_FORMAT)) == -DAYS_DIFFERENCE, "Date difference does not match"