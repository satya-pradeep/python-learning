class caliculator:
    def add(self,a,b):
        return a+b
    def mul(self,a,b):
        return a*b
c=caliculator()
print(c.add(5,3))
print(c.mul(2,3))

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        return f"my name is {self.name} and my age {self.age}"
p1=person("satya",21)
print(p1.info())

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bhd(self):
        self.age += 1
        print(f"my name is {self.name} and my age {self.age}")
p1= person("satya",21)
p1.bhd()
p1.bhd()
p1.bhd()


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} {self.age}"
p1=person("pradeep",21)
print(p1)
