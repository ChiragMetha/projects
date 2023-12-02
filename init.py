class p1:
    def __init__(self,name,age):
        self.name=(name)
        self.age=(age)
    def myfunc(self):
        print("My name is "+ self.name)
            
person = p1("chirag",23)
person.myfunc