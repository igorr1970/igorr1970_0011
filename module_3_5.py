def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        # Извлекаем первую цифру и преобразуем её в целое число
        first = int(str_number[0])
        # Рекурсивно вызываем функцию для оставшихся цифр
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если длина строки 1, возвращаем единственную цифру
        return int(str_number)


# Пример использования функции
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24