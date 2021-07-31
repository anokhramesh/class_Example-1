class Employees:# Created a class name -Employees
    def __init__(self,name,age,grade,d_o_b,job,nationality,service):#initilize methods /attributes
        self.name =name
        self.age = age
        self.grade = grade
        self.d_o_b = d_o_b
        self.job = job
        self.nationality = nationality
        self.service = service

    def details_E16384(self):# Created a function to print the detaisl of Employee E_16384
        print("Name of Employee # 16384 is",E_16384.name)
        print("Age of Employee # 16384 is",E_16384.age,"Years")
        print("Grade of Employee # 16384 is",E_16384.grade)
        print("Date of Birth of Employee # 16384 is", E_16384.d_o_b)
        print("Job of Employee # 16384 is",E_16384.job)
        print("Nationality of Employee # 16384 is",E_16384.nationality)
        print("Service of Employee # 16384 is",E_16384.service,"Years")


E_16384 =Employees("Ramesh",50,"P0205","17/jan/1971","Cable Jointer","Indian",17)#Created an object name E_16384

E_16384.details_E16384()# calling the  function with object name .function name