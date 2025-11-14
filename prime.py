
n=int(input('enter a number: '))
flag=False
if n==1:
    print('not prime number')
elif n>1:
    for i in range(2,n):
     if(n%i==0):
      flag=True
      break
if flag:
  print("not a prime number")
else:
    print("it's a prime number")


#Print all Prime Numbers in an Interval 
l=int(input('enter a initial number: '))
u=int(input('enter a upper number: '))
print('prime numbers between',l,'and',u)
for n in range(l,u+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)     
