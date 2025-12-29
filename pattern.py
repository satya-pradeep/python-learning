#pattern
n=5
for i in range(1,n+1):
    print(i*"*")

n=5
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))


n=5
for i in range(n):
    for j in range(n):
        print("* ",end='')
    print()



n=5
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
for j in range(n-1,0,-1):
    print(" "*(n-j)+"*"*(2*j-1))

