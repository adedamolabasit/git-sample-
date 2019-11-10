print('sign up')
name=input('name: ').lower()
try:
    number=int(input('mobile number: '))
except ValueError:
    print('INVALID NUMBER!!!')
email_address=input('email address:  ')
password=(input('password: ').lower())
limit=6
above_limit=15
space=(""" """)
if len(password)<limit:
    print(F'''the password is too weak
password must not be less than six''')
elif len(password)>above_limit:
    print('the password is too long')
else:
    count=1
    count_limit=3
    while count <= count_limit:
        confirmed_pass = input('confirm password')
        if confirmed_pass==password:
            count+=1
            print('password approved')
            break
        else:
            print("password does not match!!!")
print('signed in...')
menu1="""Bet wisely...
Evaluate your budget...
Take life to the fullest...
BET...BET...BET"""
print(space)
print(F'''{name} welcome to BETarena,
check your email account @   {email_address}  to verify you email account or''')

menu2=f"""                  MENU                           BETare#a
                     are#a1   [GUESSYOURMIND]                STAKE:
                                Range[1-100]                  odd:x22.6
                                3 trials                                 """
guess_count=1
secret_no=56
guess_limit=4
try:
    stake=int(input(f'stake: '))
except ValueError:
    print('GUESS A NUMBER !!!')
print(space)
print(menu2)
print(space)
won=False
while guess_count<guess_limit:
    guess_count+=1
    money=stake*22.6
    guess=int(input(f"GUESSYOURMI#D:  "))
    if guess==secret_no:
         print('you won!!!')
         print(f"your account has been credited with #{money}")
         break

    elif guess!=secret_no:
        print('you loose!!!')
        print(space)
        print(menu1)
print(space)
print('THANK YOU FOR BETTING WITH BETarena')







