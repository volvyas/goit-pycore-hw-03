# Вимоги до завдання:

# Параметр функції phone_number — це рядок з телефонним номером у різноманітних форматах.
# Функція видаляє всі символи, крім цифр та символу '+'.
# Якщо міжнародний код відсутній, функція додає код '+38'. Це враховує випадки, коли номер починається з '380' (додається лише '+') 
# та коли номер починається без коду (додається '+38').
# Функція повертає нормалізований телефонний номер у вигляді рядка.

import re


def normalize_phone(phone_number):
    normalized_phone = re.sub(r'[^\d|+]', '', phone_number)
    if(normalized_phone.startswith("38")): 
        normalized_phone = '+' + normalized_phone
    elif(normalized_phone.startswith("0")): 
        normalized_phone = '+38' + normalized_phone
    return normalized_phone

#Checks
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:")
print("\n".join(sanitized_numbers))


assert sanitized_numbers[0] == '+380671234567'
assert sanitized_numbers[4] == '+380501233234'