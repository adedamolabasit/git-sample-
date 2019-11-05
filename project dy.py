from random import randint
print("guess an integer number from the range of (100)\nenter 'HINT' if you need any help or enter any key if you don't need help")
hint=input('hint').lower()
a=randint(1,100)
b='YOU ARE NOT HINTED!!!'
if a<20 :
    if hint=='hint':
        print('the number is between (o and 19)')
    else:
        print(b)
if a>20 and a<=40:
    if hint=='hint':
        print('the number is between (20 and 40)')
    else:
        print(b)
if a>40 and a<=60:
    if hint=='hint':
        print('the number is between (40 and 60)')
    else:
        print(b)
if a>60 and a<=80:
    if hint=='hint':
        print('the number is between (60 and 80)')
    else:
        print(b)
if a>80 and a<=100:
    if hint=='hint':
        print('the number is between (80 and 100')
    else:
        print(b)
guess=None
guess_count=3
guess_limit=1
print(a)
try:
    guess=int(input('guess:'))
    while guess!=a and guess_count>guess_limit:
        guess=input('guess')
        guess_count-=1

        print(f'ypu are left with')
except:
    print("enter HINT for help\nEnter a valid integer number")
if guess==a:
    print('you won')
else:
    print(f'the correct answer is {a}')


