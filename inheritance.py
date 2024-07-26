class faculty:
    def __init__(self,f_name,department,f_id):
        self.f_name=f_name
        self.department=department
        self.f_id=f_id
    def info(self):
        print("Faculty information=",self.f_name,self.department,self.f_id)
obj=faculty("bhavani madam","IT",1001)
obj.info()
class department(faculty):
    pass
obj1=department("mohan sir","IT",1002)
obj1.info()
