def  get_multiplied_digits(number):
    str_number = str(number) # запишите строковое представление(str) числа number в неё.

    first = int(str_number[0]) #первый символ из str_number в числовом представлении(int).
    if len(str_number) > 1:
        return first *  get_multiplied_digits(int(str_number[1:])) # Возвращайте значение f
    else:
        return int(str_number)

result = get_multiplied_digits(40203)

print(result)

result2 = get_multiplied_digits(402030)

print(result2)
