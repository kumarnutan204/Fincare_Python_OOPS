class Employee:
    raise_amount=1.04
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first + '.' + last +'@company.com'
        Employee.num_of_emp+=1
        
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay= int(self.pay*self.raise_amount)
        return self.pay
    
    

dev1=Employee('Nutan','Kumar', 90000)
dev2=Employee('A', 'B', 30000)

print(dev1.email)
print(dev2.email)


