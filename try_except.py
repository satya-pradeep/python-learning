#Try and Except
# Try = the try bllock lets you test a block of code for errors
# Except = the Excepts block you handle the errors
# the else block lets execute the code if ther is no errors
# The finally block lets you execute code, regardless of the result of the try- and except blocks.


# Exception Handling
# When an error occurs,Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:

'''a = 5
b = 0
try:
    print(a/b)
except:
    print("Divided by zero is not possible")'''

'''try:
    print(x)
except:
    print("Nothing")'''

#using else
'''try:
    print("Hi")
except:
    print("something error")
else:
    print("ther is no error")'''

#finally
#The finally block gets executed no matter if the try block raises any errors or not:

'''try:
    print('x')
except:
    print("ther is an error")
finally:
    print("the'Try except' is finished")'''
