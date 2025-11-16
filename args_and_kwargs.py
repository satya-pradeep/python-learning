#*args
def add(*numbers):
    sum=0
    for i in numbers:
        sum +=i
    print(sum)
n=list(map(int ,input("enter a numbers").split(",")))
n=[1,2,3]
add(*n)

#**kwargs
def info(**person):
    for i,j in person.items():
        print(i,j)
info(name="pradeep",age=21)
info(name="ram",age=20)
