# kirill kulbitskiy, просим пользователя ввести текст
text = input("Введите текст: ")

# Разбиваем текст на отдельные слова
words = text.split()

# Счётчик для подсчёта слова 'Python'
count = 0

# Перебираем все слова в тексте
for word in words:
    if word == "Python":
        count += 1

# Выводим результат
print("Слово 'Python' встречается", count, "раз(а).")