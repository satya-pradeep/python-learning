a = int(input("enter your age: "))
license = input("enter True or False: ")

# Convert string to actual boolean
license = license.lower() == "true"

if a >= 18:
    if license:
        print("you can drive")
    else:
        print("you need license")
else:
    print("not eligible")
