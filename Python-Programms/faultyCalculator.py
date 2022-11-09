print('Enter a number: ')
num1 = int(input())

print('Enter another number: ')
num2 = int(input())

print('Enter which operation you want to perform: ')
opr = input()

if num1 == 56 and num2 == 9 and opr == 'add':
    print('addition of two numbers is ', 77)

if num1 == 43 and num2 == 3 and opr == 'mul':
    print('multiplication of two numbers is ', 79)

if opr == 'add':
    print('addition of two numbers is ', num1+num2)
elif opr == 'sub':
    print('substraction of two numbers is ', num1-num2)
elif opr == 'mul':
    print('multiplication of two numbers is ', num1*num2)
elif opr == 'div':
    print('division of two numbers is ', num1/num2)




