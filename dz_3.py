num_1 = int(input('Введите первое число диапозона: '))
num_2 = int(input('Введите второе число диапозона: '))

for i in range(num_1, num_2 + 1):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print('Fizz Buzz')