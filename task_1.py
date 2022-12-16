# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = abs(float(input('Введите вещественное число: ')))

while number % 10 != 0:
    number = round((number * 10),13)


number = int(number)
count = 0

while number != 0:
    count = count + number % 10
    number = number // 10

print(count)