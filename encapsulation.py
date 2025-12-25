#encapsulation
class person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
p1=person("sai",20)
print(p1.name)
print(p1.age)

#2
class person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get(self):
        return self.__age
p1=person("sai",20)
print(p1.name)
print(p1.get())

# 3setter method
class person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get(self):
        return self.__age
    def set(self,age):
        if age>0:
            self.__age=age
        else:
            print("age is must be positive")
            
p1=person("sai",20)
print(p1.name)
print(p1.get())

p1.set(28)
print(p1.get())
