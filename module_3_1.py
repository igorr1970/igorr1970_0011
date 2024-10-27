calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()  # Увеличиваем счётчик вызовов
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (length, upper_case, lower_case)

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счётчик вызовов
    # Проверяем наличие строки в списке без учета регистра
    for item in list_to_search:
        if item.lower() == string.lower():
            return True
    return False

# Примеры вызовов функций
print(string_info('Capybara'))  # (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon'))  # (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True
print(is_contains('cycle', ['recycling', 'cyclic']))  # False

# Вывод количества вызовов
print(calls)  # Выводит количество вызовов

