num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
count = 0

for i in range(num_1, num_2 + 1):
    print('Все числа диапозона заданных чисел: ', i, end='\n')
for j in range(num_2, num_1 -1, -1):
    print('Все числа диапозона в обратном порядке: ', j, end='\n')
for x in range(num_1, num_2 + 1):
    if(x % 7 == 0):
        print('Все числа кратные 7: ', x, end='\n')
for s in range(num_1, num_2 + 1):
    if s % 5 == 0:
        count += 1
        print('Количество символов, делящихся на 5: ', count, end='\n')