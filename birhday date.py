birthday={'becky':'12/06/19**','adedamola':'15/08/19**','doyin':'6/11/19**'}
while True:
    name=input('enter a name(blank to quit )')
    if name =='':
        break
    elif name in birthday:
        print(birthday[name])
    elif name not in birthday:
        print('the name given is not in the birthday database')
        print('enter a name to update the database')
        db=input('date_of_birth')
        birthday[name]=db
        print('The birthday database has been updated')
    elif name==None:
        print('fill the blank space appropriately')


