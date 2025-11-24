#iterator list
x=[1,2,3,4]
y=iter(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))

#string
z='banana'
a=iter(z)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

#for loop
n=(10,20,30,40)
m=("Apple","bag")#if we give as list or tuple it give each word
for i in n:
    print(i)
for j in m:
    print(j)

s=('pradeep')#if we give only one string it will each character in letter
for k in s:
    print(k)

