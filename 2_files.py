"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    text = ''
    # reading local file
    with open('./referat.txt', 'r', encoding='UTF-8') as f:
        text = f.read()
    
    print(f'Text contains {len(text)} words')

    text = text.replace('.', '!')

    # writing modified file
    with open('./referat2.txt', 'w', encoding='UTF-8') as f:
        f.write(text)

if __name__ == "__main__":
    main()
