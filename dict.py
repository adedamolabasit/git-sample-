dic={'akinpelu':'adedamola','dada':'ebin','ibitua':'michael'}
a=[]
for k,v in dic.items():
    print(f'key:{k}\tvalue:{v}')

message='it was a bad day in april .and the clock were striking thirteen. '
count={}
for value in message:
    count.setdefault(value,0)
    count[value]=count[value]+1
print(count)
