#armstrong number
n = 9474
t = n
total = 0
l = len(str(n))
while n != 0:
    d = n % 10
    total = d**l + total
    n = n//10
if total == t:
    print("Armstrong number")
else:
    print("not a Armstrong number")

#fibanocci
n = 10

a = 0
b = 1
for i in range(1,n+1):
    a,b = b,a+b
    print(a,end = ',')


#reverse
n = 1234
r = 0
t = n
while n != 0:
    d = n % 10
    r = r*10 + d
    n = n // 10
print(r)


#palindrome
n = 121

temp = n
r = 0

while n != 0:
    d = n%10
    r = r*10 +d
    n = n//10
if r == temp:
    print("palindrome")
else:
    print("not palindrome")

#prime numbers up to n
n = int(input("enter a number: "))
for i in range(2,n+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i,end = ",")

#prime number
n = int(input("enter a number: "))
c = 0
for i in range(1,n+1):
    if n % i == 0:
        c += 1
if c == 2:
    print("prime")
else:
    print("not a prime")
