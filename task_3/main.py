with open('text.txt', 'r', encoding='utf-8') as f: # kirill kulbitskiy, открываем файл под псевдонимом f
    text = f.read() # читаем весь текст из файла
    words = text.split() # разделяем текст на слова
print(f'Количество слов в файле: {len(words)}') # выводим количество слов в нем