def print_params(a=1, b='строка', c=True):
    print(a, b, c)



print_params()  # Функция должна выводить эти параметры.

print_params(4)  # меняем аргумент a
print_params(b=25)  # Проверьте, работают ли вызовы перепресваиваем b
print_params(c=[1, 2, 3])  # Проверьте, работают ли вызовы  перепрсваиваем  с
print() #Распаковка параметров:
values_list = [3, 5.45, 'Line']  # Создайте список values_list с тремя элементами разных типов.
values_dict = {'a': 1, 'b': 'строка' , 'c': True} # Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params
print_params(*values_list) # Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(*values_dict) # Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(**values_dict) # Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря)
print() # Распаковка + отдельные параметры:
values_list_2 = [7.62, 88]
print_params(*values_list_2) #  True из верхнего списка
print_params(*values_list_2, 42)  #Проверьте, работает ли print_params(*values_list_2, 42)
def a(my_list = []):
    