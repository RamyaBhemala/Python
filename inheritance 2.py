#create a class of name placements which has a function info which displays no of placements.create another class name department with function display which will display the names
#of departments present in the college.create a class pragati with a function welcome which displays the message welcome to pec wea re glad to have u onboard.pragati class should also
#display the details about departments and placements
class placements:
    def info(self):  
        print("the number of placements are 685 and still counting")
class department(placements):
    def display(self):
        print("the departments are:\n CSE\n IT\n EEE\n ECE\n Civil")
class pragati(department):
    def welcome(self):
        print("welcome to pragati engineering college we are glad to have u onboard")
obj1=pragati()
obj1.welcome()
obj1.display()
obj1.info()


