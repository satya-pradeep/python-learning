#import math
import math
a=min(2,4,6,8,1)
b=max(2,4,6,8,1)
c=abs(-7)
h=pow(4,3)
d=math.sqrt(81)
f=math.ceil(1.4)
g=math.floor(1.4)
e=math.pi
print(a,b,c,d,e,f,g,h)

#try and except 
try:
    print(x)
except:
    print('hi')
finally:
    print("there was an error in the code")

#2 example
try:
    print("satya")
except:
    print("pradeep")
else:
    print("ther is no error")

#json
import json
x='{"name":"satya","age":21}'
y=json.loads(x)
print(y["age"])
