#factorial 
n=int(input("enter a number: "))
f=1
if n < 0:
    print('not valid')
elif n==0:
    print('1')
else:
    for i in range(1,n+1):
        f*=i
    print(f)
