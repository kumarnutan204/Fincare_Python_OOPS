class Employee:
    raise_amount=1.04
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first + '.' + last +'@company.com'
        
        
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay= int(self.pay*self.raise_amount)
        return self.pay
    

class Developer(Employee):
    raise_amount=1.10
    def __init__(self,first,last,pay,prog_lang):
        #use either of the statemaents to refer to the parent class 
        #super().__init__(first,last,pay,prog_lang)
        #Employee.__init__(self,first,last,pay,prog_lang)
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang
            
class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullname())
            
            
            

dev1=Developer('Nutan','Kumar', 90000,'Python')
dev2=Developer('A', 'B', 30000,'Java')

mgr1=Manager('Sue','Smith',90000,[dev1])



#Python has functions to check if instance is of a specific class

print(isinstance(mgr1,Manager))#:::: should be true as mgr 1 is an instance of Manager

print(isinstance(mgr1,Developer))

#issubclassfunction
print(issubclass(Developer,Employee))#should be true as developer is a subclass of Employee

print(issubclass(Manager, Developer))#False







# print(mgr1.email)

# mgr1.add_emp(dev2)
# mgr1.print_emp()
# mgr1.remove_emp(dev2)
# mgr1.print_emp()



# print(dev1.email)
# print(dev1.prog_lang)

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)


