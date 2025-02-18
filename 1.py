from csv import reader

count = 0
with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for stroka in table:
        name = stroka[1]
        if len(name) > 30:
            count += 1

    print(f'Найдено {count} книг')