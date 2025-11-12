#Even & Odd Counter
n=list(map(int, input("enter a list of numbers: ").split(',')))
e_c=0
o_c=0
for i in n:
    if i%2==0:
        e_c+=1
    else:
        o_c+=1
       
print(e_c)
print(o_c)

#Find the Largest and Smallest
n=list(map(int, input("enter a list: ").split(',')))
s=n[0]
l=n[0]
for i in n:
    if i<s:
        s=i
    if i>l:
        l=i
print(s)
print(l)
#2
n=list(map(int,input("enter a list: ").split(",")))
n.sort()
print(n[0])
print(n[-1])

#3
n=list(map(int,input("enter a list: ").split(",")))
print(min(n))
print(max(n))


#find duplicates
n=list(map(int,input("enter a list: ").split(",")))
d=[]
for i in n:
    if n.count(i)>1:
        if i not in d:
            d.append(i)
if d:
    print(d)
else:
    print("no duplicates")

#unique numbers
n=list(map(int,input("enter a list: ").split(",")))
u=[]
for i in n:
    if i not in u:
        u.append(i)
print(u)
