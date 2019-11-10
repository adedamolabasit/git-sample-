secret_no=7
guess_count=1
guess_limit=3
sign_up='sign up'
output='signed in'
welcome='you are welcome to BETarena'
print(sign_up)
name=input('name: ')
number=input('phone no: ')
email=input('email address: ')
print(output)
print(f"""{name} you are {welcome}
Bet wisely...
Evaluate your budget...
Take life to the fullest...
BET...BET...BET""")
menu=f"""                  MENU                           BETare#a
                     are#a1   [GUESSYOURMIND]                STAKE:
                                Range[1-100]                  odd:
                                5 trials                     [1#=X5.0],[2#=X10.0],[3#=X20.0],[4#=X30.0],[5#=X40.0]

                     are#a2   [GUESSYOURMIND]                STAKE:
                              Range[100-500]                  odd:
                               4 trials                     [1#=X15.0],[2#=X30.0],[3#=X45.0],[4#=X65.0]

                     are#a3   [GUESSYOURMIND]                STAKE:
                              Range[500-1000]                  odd:
                                3 trials                     [1#=X30.0],[2#=X60.0],[3#=X90.0]
                     are#a4  [GUESSYOURMIND]                STAKE:
                             Range[1000-2000]                  odd:
                                2 trials                     [1#=X150.0],[2#=X300.0]
                     are#a1   [GUESSYOURMIND]               STAKE:
                              Range[2000-3500]                  odd:
                                1 trials                     [1#=X500]"""
print(menu)
user =(input('enter your arena  no >>>   '))
arena1 = """ are#a1   [GUESSYOURMIND]                STAKE:
                                   Range[1-100]                  odd:
                                   5 trials                     [1#=X5.0],[2#=X10.0],[3#=X20.0],[4#=X30.0],[5#=X40.0]"""
if user.lower=="arena1":
    print('arena1')

















