exam=input('what is your exam score')
test=input('what is your test score ')
result= int(exam)+int(test)
print(f" {result} + %")
simple=True
if result>=70:
    print('A')
    print('excellent')
elif result>=60<=70:
    print('B')
    print('very good')
else:
    print('''you should have done better tha this
    i guessed you score an A or b
    enjoy your day!!!''')
print('first semester result')
print('FINAL GRADE')


