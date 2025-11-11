print("Simple Calculator")
print("Type 'exit' anytime to stop.\n")

while True:
    n1 = input("Enter first number: ")
    if n1.lower() == "exit":
        print("Calculator closed.")
        break

    n2 = input("Enter second number: ")
    if n2.lower() == "exit":
        print("Calculator closed.")
        break

    # convert inputs to numbers
    n1 = float(n1)
    n2 = float(n2)

    print("Select operation: +  -  *  /")
    r = input("Enter operation: ")

    if r == "+":
        print("Result:", n1 + n2)
    elif r == "-":
        print("Result:", n1 - n2)
    elif r == "*":
        print("Result:", n1 * n2)
    elif r == "/":
        if n2 != 0:
            print("Result:", n1 / n2)
        else:
            print("Error: Division by zero not allowed!")
    else:
        print("Invalid operation!")

    print("-" * 30)  
