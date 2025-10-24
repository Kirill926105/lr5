print('Введите строки(текст): ') # kirill kulbitskiy, вводим строки(текст)
lines = []
while True: # 
    line = input()
    if line == '':
        break
    lines.append(line)
print('\nРезультат:') # 
for line in lines:
    if len(line) > 1: # если длина введенного текста > 1, то меняем местами первую и последнюю буквы
       new_line = line[-1] + line[1:-1] + line[0]
    else: #
       new_line = line
print('Измененный текст:', new_line) #