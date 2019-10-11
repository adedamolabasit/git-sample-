n=int(input('enter number '))
temp=n
rev=0
while (n>0):
     dig=n%10
     rev=rev*10+dig
     n=n//10
if(temp==rev):
    print('the number is a palindrome!')
else:
    print("the number isn't palindrome")
e=n+rev
print(e)

n=int(input('input any number '))
val=0
if  n>0:
     num=n%10
     fir=n//10
     a=fir+num
print(a)
k=[]
lower=int(input('enter lower range '))
upper=int(input('enter upper range'))
divisor=int(input('enter number to be divided by'))

for i in range(lower,upper):
     if i%divisor==0:
         k.append(i)
print(k)
inte=int(input('enter an integer number '))
a=[]
for i in range(2,inte+1):
    if inte%i==0:
        a.append(i)
    a.sort()
print(a[0])
