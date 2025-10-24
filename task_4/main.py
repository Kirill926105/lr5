print("Введите несколько строк (после последней просто нажмите Enter на пустой строке):") # kirill kulbitskiy, ввод строк

# Собираем все строки в список
lines = []
while True:
    line = input()
    if line == "":  # если пользователь просто нажал Enter — заканчиваем ввод
        break
    lines.append(line)

# Обрабатываем каждую строку
print("\nИзменённые строки:")
for line in lines:
    if len(line) > 1:
        # Меняем первую и последнюю букву местами
        new_line = line[-1] + line[1:-1] + line[0]
    else:
        # Если строка короткая, оставляем как есть
        new_line = line

    print(new_line) # выводим результат