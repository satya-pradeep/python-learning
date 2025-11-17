#lambda with built function
#map()
n=[1,2,3,4]
doubled=list(map(lambda a:a*2,n))
print(doubled)

#filter()
m=[1,2,3,4,5,6,7,8,9,10]
f=list(filter(lambda a: a%2!=0,m))
print(f)

#sorted()
student=[('satya',20),('diwa',29),('hemu',22)]
s=sorted(student,key=lambda a:a[1])
print(s)
