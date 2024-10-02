First = int(input('Ввод: '))
Second = int(input('Ввод: '))
Third = int(input('Ввод: '))
if First == Second == Third:
    print('Вывод: 3')
elif First == Second or First == Third or Second == Third:
    print('Вывод: 2')
else:
    print('Вывод: 0')