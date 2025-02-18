from csv import reader


output = open('books_result.txt', 'w', encoding='windows-1251')

with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    count=0
    table = reader(csvfile, delimiter=";")
    for stroka in table:
        count+=1
        if count>1:
            print(f'{stroka[3]}. {stroka[1][1:]} - {stroka[6][6:][:4]}\n')
            output.write(f'{stroka[3]}. {stroka[1][1:]} - {stroka[6][6:][:4]}\n')
        if count==21:
            break

output.close()