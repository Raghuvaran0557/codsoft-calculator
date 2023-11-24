def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y !=0:
        return x / y
    else:
        return "Cannot divide by zero."
while True:
    try:
        first_input=float(input("Enter the first number: "))
        second_input=float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue
    print("\nSelect operation:")
    print("1-> Add")
    print("2-> Subtract")
    print("3-> Multiply")
    print("4-> Divide")
    print("5-> Exit")
    choice=input("Enter choice (1/2/3/4/5): ")
    if choice=='1':
        result=add(first_input,second_input)
        print(f"\n{result}")
    elif choice=='2':
        result=subtract(first_input,second_input)
        print(f"\n{result}")
    elif choice=='3':
        result=multiply(first_input,second_input)
        print(f"\n{result}")
    elif choice=='4':
        result = divide(first_input,second_input)
        print(f"\n{result}")
    elif choice=='5':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 5.")
