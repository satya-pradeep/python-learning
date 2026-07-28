#for loop 
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#A for for loop is used when you know how many times you want to iterate over a block of code.

for i in range(5):
    print(i)

a = [1, 2, 3, 4, 5]
for i in a:
    print(i**2)

f = ['apple','banana','cherry']
for i in f:
    print(i)

n = 'pradeep'
for i in n:
    print(i,end=' ')

x = (1,2,3,4)
for i in x:
    print(i)

data = {"name":'pradeep',"age":21}
for i in data:
    print(i)
print(data["name"],data['age'])

a = [1,2,3,4]
a.sort(reverse=True)
print(a)

b=['a','b','c']
b.reverse()
print(b)

for i in range(1,11):
    i.reverse()
    print(i)

#print numbers from 1 to 10
for x in range(1,11):
    print(x)

#print numbers from 10 to 1
for i in range(10,0,-1):
    print(i)

#'''print even numbers bw 1 to 20
for i in range(1,21):
    if i%2==0:
        print(i)

#print odd numbers bw 1 20
for i in range(1,21):
    if i%2!=0:
        print(i)

#5 table
n=5
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

#sum of numbers from 1 to 100
t=0
for i in range(1,101):
    t=t+i
print(t)


#sum of all even numbers from 1 to 50
t=0
for i in range(1,51):
    if i%2==0:
        t=t+i
print(t)

#sum of all odd numbers from 1 to 50
t=0
for i in range(1,51):
    if i %2!=0:
        t=t+i
print(t)

#factorial of a number
n=10
f=1
for i in range(1,n+1):
    f=f*i
print(f)  

#print every element
n = [2, 4, 6, 8, 10]
for i in n:
    print(i)

#sum of all elements
n = [2, 4, 6, 8, 10]
t=0
for i in n:
    t=t+i
print(t)

#largest & smallest element
n = [2, 4, 6, 8, 10]
print(max(n))
print(min(n))

#Count how many elements are in the list
n =[2,4,6,8,10]
m=len(n)
print(m)

n = [2,4,6,8,10]
c=0
for i in n:
    c += 1
print(c)

#Print the square of every element.
n = [2,4,6,8,10]
for i in n:
    s=i**2
    print(s,end=' ')


#prime number or not
n=4
if n<=1:
    print('not a prime number')
else:
    for i in range(2,n):
        if n%i==0:
            print('not a prime')
            break
    else:
        print('prime number')

#print prime numbers in bw 1 to 100
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i, end=' ')


#patterns
n=5
for i in range(1,n):
    m=i*'*'
    print(m)

for i in range(n,0,-1):
    m=i*'*'
    print(m)

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=' ')
    print()


#largest number
a = [12, 45, 3, 67, 23]
n=len(a)
for j in range(n):
    for i in range(0,n-j-1):
        if a[i] > a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
print(a[0])
print(a[-1])

a = [12,45,3,67,23]
s=a[0]
l=a[0]
for i in a:
    if i>l:
        l=i
    if i<s:
        s=i
print(l)
print(a[1])
print(s)


#star_pattern
'''
*
**
***
****
*****
'''
n=5
for i in range(1,n+1):
    print(i*'*')

'''
     *
    ***
   *****
  *******
 *********'''
n=5
for i in range(1,n+1):
    print((n-i)*' ',(2*i-1)*'*')

'''
 *********
  *******
   *****
    ***
     *'''
n=5
for i in range(n,0,-1):
    print((n-i)*' ',(2*i-1)*'*')

'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * '''
r,c=5,5
for i in range(1,r+1):
    for j in range(1,c+1):
        print('*',end=' ')
    print()
