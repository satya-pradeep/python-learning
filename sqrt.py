#1
import math
n=int(input('enter a number: '))
r=int(math.sqrt(n))
print(r)

#2
n=9
r=n**0.5
print(r)

#3
class sqrt:
    def sqr(self,x):
        odd=1
        count=0
        while x>0:
            x=x-odd
            odd=odd+2
            count +=1
        
        if x==0:
            return count
        else:
            return "not a perfect square"
n=sqrt()
r=n.sqr(20)
print(r)
