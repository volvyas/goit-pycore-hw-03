#Вимоги до завдання:
#
#1. Параметри функції:
#
#min — мінімальне можливе число у наборі (не менше 1).
#max — максимальне можливе число у наборі (не більше 1000).
#quantity — кількість чисел, які потрібно вибрати (значення між min і max).
#2. Функція генерує вказану кількість унікальних чисел у заданому діапазоні.

#3. Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. 
# Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.

import random as r

def get_numbers_ticket(min, max, quantity):
    result_list = list()
    if(min < 1): 
        print("Min cannot be less than 1")
        return result_list
    elif(min > max): 
        print("Min cannot be greater than max")
        return result_list
    elif(max > 1000): 
        print("Max cannot be greater than 1000")
        return result_list
    elif(quantity < min or quantity > max):
        print("Quatnity must be between Min and Max")
        return result_list

    return sorted(r.sample(range(min, max+1), quantity))
    

#Usage
print(get_numbers_ticket(1,100, 6))

