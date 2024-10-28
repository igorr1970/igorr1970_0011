def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        # Извлекаем первую цифру и преобразуем её в целое число
        first = int(str_number[0])
        # Если первая цифра не равна нулю, умножаем её на результат рекурсии
        if first != 0:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            # Если первая цифра равна нулю, пропускаем её и продолжаем с оставшимися цифрами
            return get_multiplied_digits(int(str_number[1:]))
    else:
        # Если длина строки 1, возвращаем единственную цифру, если она не равна нулю
        return int(str_number) if str_number != '0' else 1

# Пример использования функции
result = get_multiplied_digits(402030)
print(result)  # Вывод: 24