size=input("what size pizza you want (S/M/L)? ")
bill=0

if size=='S' or size=='s':
    bill+=100
    print("small pizza price is 100")
elif size=='M' or size=='m':
    bill+=200
    print("Medium pizza price is 200")
else:
    bill+=300
    print("Large pizza price is 300")

add_pepperoni=input("do you want any pepperoni (Y/N)?")
if add_pepperoni=="Y" or add_pepperoni=='y':
    if size=="s" or size=='S':
        bill+=20
    else:
        bill+=30

extra_cheese=input("do you want extra cheese(Y/N)?")
if extra_cheese=='y' or extra_cheese=="Y":
    bill+=20
print(f"your final bill is {bill}")



