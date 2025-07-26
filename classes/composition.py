
#Aggregation 

class Salary:
    def __init__(self,currency,amount):
        self.currency=currency
        self.amount=amount

class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary=salary
        
 
salary1 = Salary(currency='euros',amount =800) 
employee1  =  Employee('Homelander',salary1)

print(employee1.name)
print(employee1.salary.amount)
print(employee1.salary.currency)

       

        
        
      
        