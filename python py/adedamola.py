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

#price of a house is $1M
#if buyer has good credit,they need to put down 10% otherwise they need to put down 20%
price=1000000
good_credit=False
if good_credit:
    reduction=price*(10/100)
    print(f"{reduction} is our offer for you")
else:
    reduction=price*(20/100)
    print(f"believe me{reduction} is our best offer ")
print('thanks for doing business with us ')

