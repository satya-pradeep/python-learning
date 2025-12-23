#factorial
n=5
f=1
for i in range(1,n+1):
    f=f*i
print (f)

#fibonacci 
n=7
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,b+a
#2
n=7
a,b=0,1
i=0
while i<n:
    a,b=b,b+a
    i+=1
print(a)


#reverse a string
n='sai'
print(n[::-1])

#reverse a number
n='123'
print(n[::-1])

#2
n=246
r=0
while 0<n:
    r=r*10+n%10
    n//=10  #n=n//10
print(r)


#palindrome
n=121
temp=n
r=0
while 0<n:
    r=r*10+n%10
    n//=10
if temp==r:
    print("yes")
else:
    print("no")

#2
n=input("enter a number:")
n=str(n)
if n==n[::-1]:
    print("yes")
else:
    print("no")

