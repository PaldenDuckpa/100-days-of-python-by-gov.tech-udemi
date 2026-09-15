
class Employee:
    def __init__(self,first,last,pay):
        self.first = first 
        self . last = last 
        self . pay = pay
        self.email = first + '-' + last + '@gmail.com'
        
    def fullname(self):
        return '{} {}' .format(self.first,self.last)  
    
    
emp_1 = Employee('sonam','dorji',5000)
emp_1 = Employee('tashi','dorji',5000)  
print(Employee.fullname(emp_1))
print(emp_2.fullname())

