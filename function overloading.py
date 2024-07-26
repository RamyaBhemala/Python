#nfunction overloading is not allowed in python.so,it considers only last function
class arithmetic:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
obj=arithmetic()
#obj.add(10) #produces error
#obj.add(10,20) #produces error
obj.add(3,2,9)
