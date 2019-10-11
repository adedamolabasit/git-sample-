class LivingThings:
    def __init__(self,mammals,reptiles,amphibians,apes):
        self.mammals=mammals
        self.reptiles=reptiles
        self.amphibians=amphibians
        self.apes=apes
        print(f'''{mammals}
                    {reptiles}
                    {amphibians}
                    {apes}''')
        if mammals.lower()=='goat':
            print('there are attribute and methods for goat and dog')
        elif amphibians.lower()=='toad':
            print('there are attribute and methods for frog')
        elif reptiles.lower()=='snakes':
            print('there are attribute ad methods for snakes')
        elif apes.lower()=='monkey':
            print('there are attribute and methods for monkeys')
        else:
            print('the attribute and methods for all this are gonna be make available soon')


class Mammal:
    def walk(self):
        print('walk')


class goat(Mammal):
    def bleat(self):
        print('meeh!!! meeh')


class dog(Mammal):
    def bark(self):
        print('gbogh,gbough')


animal=goat()
print(animal.walk())
all=LivingThings('rat','snakes','toad','monkey')
print(all)



