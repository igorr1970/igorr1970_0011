def single_root_words(root_word, *other_words):
    # Создаем пустой список для хранения подходящих слов
    same_words = []

    # Приводим корневое слово к нижнему регистру для сравнения
    root_word_lower = root_word.lower()

    # Перебираем все слова из other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()

        # Проверяем, содержится ли одно слово в другом
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    # Возвращаем список подходящих слов
    return same_words


# Примеры вызова функции и вывод результата
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)  # Ожидаемый вывод: ['richiest', 'orichalcum', 'richies']
print(result2)  # Ожидаемый вывод: ['Able', 'Disable']