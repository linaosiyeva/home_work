#Задано чотирицифрове натуральне число. 

#Знайти добуток цифр цього числа.
a = int(input('Please enter your four-digit number '))
p = 1
while a > 0:
    if a % 10 != 0:
        p = p * (a % 10)
    a = a // 10
print(f'Product is {p}')

#Записати число в реверсному порядку.
a = str(input('Please enter your four-digit number '))
list = list(a)
reverse = "".join(list[::-1])
print(reverse)

a = input('Please enter your four-digit number ')
print("".join(reversed(a)))

#Посортувати цифри, що входять в дане число.
a = input('Please enter your four-digit number ')
print("".join(sorted(a)))
