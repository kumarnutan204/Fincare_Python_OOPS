class Employee:
    num_of_emp =0
    raise_amount=1.04
    #Regular methods are defined below
    #init method is like a constructor of cpp
    #it initializes the variables
    
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
    
    #class methods are defined below
    @classmethod
    def set_raise_amt(cls,amount):# cls is like self form above ...mandatoryand cls instead of a class
        cls.raise_amount= amount
        
    #creating another class mathod for initialization (alternative constructor) 
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay= emp_str.split('-')
        return cls(first,last,pay)
    #static methods are just class methods but they do take a class or self as parameter
    #use @staticmethod : they dont operate on instance(objects) or the class
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or (day.weekday()==6):
            return False
        return True
            
      

#All in all
# Instance method: Used to access or modify the object state. If we use instance variables inside a method, such methods are called instance methods. It must have a self parameter to refer to the current object.
# Class method: Used to access or modify the class state. In method implementation, if we use only class variables, then such type of methods we should declare as a class method. The class method has a cls parameter which refers to the class.
# Static method: It is a general utility method that performs a task in isolation. Inside this method, we don’t use instance or class variable because this static method doesn’t take any parameters like self and cls.  
    
    

emp1=Employee('Nutan','Kumar', 90000)
emp2=Employee('A', 'B', 30000)
#For the normal self methods
# print(emp1.fullname())
# print(Employee.fullname(emp1))

# Employee.set_raise_amt(1.05)

# print(emp1.apply_raise())
# print(Employee.num_of_emp)

#for the class methods
# emp_str1="John-Doe-70000"
# emp_str2="Steve-Smith-35000"
# emp_str3="Jane-Doe-90000"


# new_emp_1 = Employee.from_string(emp_str1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# for static methods

import datetime
my_date= datetime.date(2016,7,10)
print(my_date)
print(Employee.is_workday(my_date))

