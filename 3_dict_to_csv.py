"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

def main():
    dump = [
        {'name': 'Jose Marquez Alcantara', 'age': 57, 'job': 'Mexican actor'},
        {'name': 'Elizabeth II', 'age': 95, 'job': 'Brittish pensioner'},
        {'name': 'Pikachu', 'age': 28, 'job': 'Yellow pokemon'},
        {'name': 'Gal Gadot', 'age': 36, 'job': 'Superwoman actress'},
        {'name': 'Xi Wei', 'age': 29, 'job': 'Chinese singer'},
        {'name': 'Petr Ivanov', 'age': 17, 'job': 'University student'},
        {'name': 'Simon Vixelshtein', 'age': 77, 'job': 'Too much money Inc. co-founder'},
        {'name': 'Maria Perre', 'age': 25, 'job': 'Photomodel'},
        {'name': 'Yokotsuma Karao Nagata', 'age': 44, 'job': 'even Yakuzas don\'t know'}
    ]

    with open('./dump.csv', 'w', encoding='UTF-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        writer.writerows(dump)


if __name__ == "__main__":
    main()
