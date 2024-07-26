#create a class f15 with functions lights-the colour of light which is taken as parameter to the function, fan-the speed of regulator which is taken as parameter to the function,
#and ac-room temperature and outside temperature which are taken as parameter to the function.write a 4th fun whose name is display which displays the diff in outside and room
#temperature of ac and also displays fan speed 
class f15:
    def __init__(ramya,start,end):
        ramya.start=start
        ramya.end=end
        print("class start time:",start)
        print("class end time:",end)
    def light(ramya,a):
        print("the color of light is:",a)
    def fan(ramya,b):
        ramya.b=b
        print("the speed of regulator is:",b)
    def ac(ramya,c,d):
        ramya.c=c
        ramya.d=d
        print("the rooms  temperature:",c,"the outside temperature:",d)
    def display(ramya):
        print("the difference:",ramya.d-ramya.c)
        print("fan speed:",ramya.b)
        print("class start time:",ramya.start)
        print("class end time:",ramya.end)
obj=f15(9.00,4.00)
obj.light("blue")
obj.fan(4)
obj.ac(16,32)
obj.display()
        
