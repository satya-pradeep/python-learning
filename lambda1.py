add = lambda x,y:x+y
print(add(2,3))

evenorodd = lambda x:"even" if x%2==0 else "odd"
print(evenorodd(7))

n=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda x:x%2==0,n))
print(even)

m=[1,2,3,4,5,6,7,8,9]
square=list(map(lambda x:x**2,m))
print(square)


m=[1,2,3,4,5,6,7,8,9]
for i in range (1,len(m)+1):
    print(i**2,end=" ,")
