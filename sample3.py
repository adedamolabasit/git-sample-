class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return (self.pay*12)+self.bonus


class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name=name
        self.age=age
        self.obj_salary=Salary(pay,bonus)

worker=Salary(500000,250000)
all=Employee('adedamola',21,80000,7437)
print(worker.annual_salary())
print(worker.bonus)
print(all.obj_salary.pay)


class Account:
    def __init__(self,account_name,account_no,):
        self.account_name=account_name
        self.account_no=account_no
        print(f"{account_name}{(account_no)} welcome to the bank of nigeria,thanks for banking  with us")

