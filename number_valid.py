#number validation
import re
number=input("enter your number: ")
if re.match(r'^[0-9]{10}$',number):
    print("valid")
else:
    print("not valid")
