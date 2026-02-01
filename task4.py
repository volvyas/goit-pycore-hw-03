# Вимоги до завдання:

# Параметр функції users — це список словників, де кожен словник містить ключі name (ім'я користувача, рядок)
#  та birthday (день народження, рядок у форматі 'рік.місяць.дата').
# Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. 
# Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
# Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name)
#  та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').
import datetime
from typing import Final 
from datetime import datetime as dt


DATE_FORMAT: Final =  '%Y.%m.%d'

def get_upcoming_birthdays():
    current_date = dt.today().date()
    result_list = list()
    for user in users_l:
        birthday_date = dt.strptime(user.get('birthday'), DATE_FORMAT).date()
        congrats_date = datetime.date(current_date.year, birthday_date.month, birthday_date.day)
        days_diff = congrats_date - current_date
        if(congrats_date < current_date): continue
        if(days_diff.days <= 7):
            result_list.append({'name': user.get('name'), 'congratulation_date': congrats_date.strftime(DATE_FORMAT)})
    return result_list



#Checks
users_l = [
    {"name": "John Doe", "birthday": "1985.02.3"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays_l = get_upcoming_birthdays()
print(upcoming_birthdays_l)

assert len(upcoming_birthdays_l) == 1




