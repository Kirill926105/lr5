print('Введите строки(текст): ') # kirill kulbitskiy, вводим строки(текст)
lines = []
while True: # вводим строки, пока не будет пустой и потом выйдем
    line = input()
    if line == '':
        break
    lines.append(line) # добавляем строку в список
print('\nРезультат:') # выводим строку результат
for line in lines:
    if len(line) > 1: # если длина введенного текста > 1, то меняем местами первую и последнюю буквы
       new_line = line[-1] + line[1:-1] + line[0]
    else: # если строка короткая - не меняем
       new_line = line
print('Измененный текст:', new_line) # выводим измененный текст