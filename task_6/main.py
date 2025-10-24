# kirill kulbitskiy, открываем файл text.txt для чтения
with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # читаем все строки из файла

# Создаём новый список для изменённых строк
new_lines = []

# Проходим по каждой строке и заменяем букву 'о' на 'а'
for line in lines:
    new_line = line.replace("о", "а").replace("О", "А")  # заменяем и маленькие, и большие буквы
    new_lines.append(new_line)

# Записываем изменённые строки в новый файл output.txt
with open("output.txt", "w", encoding="utf-8") as file:
    file.writelines(new_lines)

print("Готово! Файл output.txt создан.") # выводим результат