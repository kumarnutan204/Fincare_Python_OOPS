class Employee:
    
    def __init__(self,first,last):
        self.first=first
        self.last=last
        # self.email= first + '.' + last +'@company.com'
    
    #when we were using self.email = something it was a variable and now we create a function below that will return email 
    
    #we make the below function as a attribute(data member ) we can add @property decorator
     
    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"
    
    @property 
    def fullname(self):
        return f"{self.first} {self.last}"
    
    #using a setter
    @fullname.setter
    def fullname(self, name):
        first,last = name.split(' ')
        self.first=first
        self.last= last
    
    @fullname.deleter
    def fullname(self):
        print('Delete name')
        self.first=None
        self.last= None

emp1= Employee('Nutan','Kumar')
emp1.first='John'

print(emp1.first)
print(emp1.email)#no parenthesis needed while accessing because of the @property decorator

#here also we used @property decorator 
print(emp1.fullname)
#now when we want to set fullname as different name we can not do that like emp1.fullname="Hakuna Matata" it will give error as 'cant set attribute' 
# We use a setter for the above case

# now we can use the below as we have added a setter 
emp1.fullname="Hakuna Matata"

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

#now we are going to delete full name using a deleter(defined above)
del emp1.fullname





