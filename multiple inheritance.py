class ramya:
    def name(self):
        print("my name is ramya")
class place:
    def live(self):
        print("i belong to kakinada")
class info(ramya,place):
    def display(self):
        print("information:")
obj=info()
obj.display()
obj.live()
obj.name()
