class employee :
    age = 69
    salary =27347
    status ="unmarried"
    
    def __init__(self,age,salary,status):    #this get automatically called when we make object
        self.age =age
        self.salary =salary
        self.status =status
        
        
   
        
raushan = employee("24",23525255235,"married")
print(raushan.age,raushan.salary,raushan.status)
