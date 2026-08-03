# A function is a block of code which only runs when its called
# A function helps avoid code repetition
'''def name():
    print('pradeep')
name()
'''

#Creating a Function
#in python, a function is defined using the "def" keyword. followed by a function name and parentheses.
'''def my_name():
    print('pradeep')
'''

#Calling a Function
'''def my_name():
    print('pradeep')
my_name()'''
# we can call the same function multiple times
'''my_name()
my_name()'''

'''#parameter = variable, arguments = values
def add(a,b):  #a,b - parameter
    c = a+b
    print(f"sum of a,b = {c}")
add(2,3)  #2,3 arguments
'''
#types of arguments
# 1 default argument
# 2 positional argument
# 3 keyword argument
# 4 arbitrary/ variable length 
    # *args     :Accepts any number of positional arguments.
    # **kwargs  :Accepts any number of keyword arguments.


#positional arguments
#Arguments are passed in the same order as the parameters.




'''def fun():
    print("Hello Python!")
fun()'''

#add two numbers
'''def add(a,b):
    c = a+b
    print(c)
add(2,3)'''

#subtract two numbers 
'''def sub(a,b):
    c = a-b
    print(c)
sub(9,2)'''

#multiply two numbers 
'''def mul(a,b):
    c = a * b
    print(c)
mul(2,3)'''

#divide two numbers
'''def div(a,b):
    c = a/b
    print(c)
dev(10,2)'''


'''def fun(name):
    print(f" Hello {name}")
fun('pradeep')'''

#square of a number
'''s = lambda n:n*n
print(s(4))'''

#cube of a number
'''c = lambda n:n**3
print(c(2))'''

#odd or even
'''n = lambda x: 'even' if x%2==0 else 'odd'
print(n(12))'''

'''def fun(n):
    if n<0:
        print("negative")
    elif n == 0:
        print("zero")
    else:
        print("positive")
fun(2)
fun(0)
fun(-4)'''

#largest of two numbers.
'''def num(a,b):
    if a > b:
        print("a is larger")
    else:
        print("b is larger")
num(2,3)
num(10,8)'''

'''l = lambda a,b: 'a is larger' if a > b else 'b is larger'
print(l(10,7)) 
print(l(9,11))'''

#largest of three numbers.
'''def num(a,b,c):
    if a > b and a > c:
        print("a is larger")
    elif b > a and b > c:
        print("b is larger")
    else:
        print("c is larger")
num(2,3,7)
num(10,8,4)'''

#factorial of a number
'''def fac(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    print(f)
fac(5)'''

#check whether a number is prime.
'''def pri(n):
    if n <= 1:
        print('its not a prime number')
        return
    
    for i in range(2,n):
        if n%i == 0:
            print("its not a prime number")
            return
    else:
        print("prime number")
pri(7)
pri(9)
pri(23)
pri(2)'''


#sum of digits of a number.
'''def sum_of_digit(n):
    n = abs(n)
    t = 0
    for i in str(n):
        t += int(i)
    print(t)
sum_of_digit(1234)
sum_of_digit(123)
sum_of_digit(234)'''

#reverse a string
'''def revr(n: str):
    return n[::-1]
print(revr('1234'))'''

#count the vowels in a string.
'''def count_vowels(text):
    vowels = set("aeiouAEIOU")
    return sum(1 for i in text if i in vowels)
print(count_vowels("satya pradeep"))'''

#map
'''l = [1,2,4,6,5,7]
s = list(map(lambda x:x*x,l))
print(s)'''

'''l = [2,3,5,5,6]'''
'''s = list(map(lambda x:x**3,l))
print(s)'''
'''
s = list(filter(lambda x: x%2==0,l))
print(s)
'''

students = [
    ("Ram", 75),
    ("Pradeep", 90),
    ("John", 82),
    ("Sam", 68)
]
s = sorted(students,key = lambda x:x[1])
print(s)


