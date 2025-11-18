#countdown
def countdown(n):
    if n<=0:
        print("!Done")
    else:
        print(n)
        countdown(n-1)
countdown(5)

#factorial
def factorial(f):
    #Base case
    if f==0 or f==1:
        return 1
    #Recursive Case
    else:
        return f*factorial(f-1)
print(factorial(5))

#fibonacci sequence
def fibonacci(m):
    if m<=1:
        return m
    else:
        return fibonacci(m-1)+fibonacci(m-2)
print(fibonacci(7))    

#in list
def sum_list(numbers):
    if len(numbers)==0:
        return 0
    else:
        return numbers[0]+sum_list(numbers[1:])
my_list=[1,2,3,4,5]
print(sum_list(my_list))
