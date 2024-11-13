calls = 0 #Создать переменную вне функций.
def count_calls (): # сщздание функции
    global calls# глобальное простаранство
    calls+=1 # счетчик; изменепие значения переменной calls.
def string_info (string): # Создать функцию string_info с параметром string
    count_calls() #вызов функции
    return (len(string), string.upper(), string.lower()) # принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре
def is_contains (string, list_to_search): # Создать функцию is_contains с двумя параметрами string и list_to_search,
    count_calls() #вызов функции
    return string.upper() in [i.lower() for i in list_to_search]
print(string_info('Capybara')) # Пример выполняемого кода:
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic'])) 
print(calls)