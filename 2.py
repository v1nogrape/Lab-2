from csv import reader

count = 0
search = input('Введите запрос: ') #например, людмила петрановская
with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for stroka in table:
        lower_name = stroka[3].lower()
        i = lower_name.find(search.lower())
        if i!= -1 and (float(stroka[7]) <150):
            print(f'{stroka[3]} | {stroka[1]}')
            count += 1
    if count == 0:
        print('Не найдено книг.')
    else:
        print(f'Найдено {count} книг.')
