#multiple inheritence
class human:
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
    def __init__(self):
        self.eyes=2
        self.heart=1

class male:
    def flirt(self):
        print("i can flirt")
    def __init__(self,name):
        self.name=name

class boy(human,male):
    def __init__(self,name):
        male.__init__(self,name)
        human.__init__(self)
    def sleep(self):
        print("He can sleep")
    def work(slef):
        print("i can code")

b1=boy("pradeep")
print(b1.name)
print(b1.eyes)
