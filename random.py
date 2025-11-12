import random
n=input("enter names with seperate by comma: ")
m=n.split(",")
person_select=random.choice(m)
print(f"{person_select} will pay the bill")
