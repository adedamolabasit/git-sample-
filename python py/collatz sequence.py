def collatz(number):
    if number%2==0:
        return number//2
    elif number%2==1:
        return 3*number+1
try:
    while True:
        a=int(input('enter number'))
        b=collatz(a)
        print(b)
        if b==1:
            break

except Exception as e:
    print('ERROR:type(e)\nTHEY MUST BE INTEGER!!!')
