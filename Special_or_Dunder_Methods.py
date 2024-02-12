class Employee:
    raise_amount=1.04
    #anything enclosed with double underscores is called a dunder methodor a special method
    def __init__(self,first,last,pay):#this init method is a dunder method 
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first + '.' + last +'@company.com'
        
        
    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay= int(self.pay*self.raise_amount)
        return self.pay
    def __repr__(self): #unambiguous rep of the object and should be used for debugging and logging and things ::mostly use by the developers  
        return f"Employee('{self.first}','{self.last}','{self.pay}')"
    def __str__(self):# more readable representation of an object and is meant to be used as end user display
        return f"{self.fullname()} - {self.email}"
    
    def __add__(self,other):
        return self.pay +other.pay
    
    #get total umber of char in the fullname
    def __len__(self):
        return len(self.fullname())
    #here we can return "NotImplemented" which ensures that if one dunder method does not did not do the job then it finds other methods of the class to do it 
    

emp1=Employee('Nutan','Kumar', 60000)
emp2=Employee('A', 'B', 30000)

# print(emp1)
# print(repr(emp1))
# print(str(emp1))

# print(emp1+emp2)
print(len(emp1))



# #more functions 
# print(int,__add__(1,2))
# print(str,__add__('a','b'))

