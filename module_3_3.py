# 1. Функция с параметрами по умолчанию

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(10)
print_params(10, 'новая строка')
print_params(b = 25)
print_params(c = [1, 2, 3])

# 2.Распаковка параметров:

values_list = [3.14, 'пример', False]

values_dict = {'a': 42, 'b': 'тест', 'c': None}

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:

values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)
