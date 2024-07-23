print("Welcome to the Basic Calculator!")
print("You can perform addition (+), subtraction (-), multiplication (*), and division (/).")
print("Type 'exit' to quit the calculator.")

while True:

    first_number = input("Enter the first number: ")
    
    if first_number.lower() == 'exit':
        print("Thank you for using the calculator. Goodbye!")
        break
    
    try:
        
        first_number = float(first_number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    
    operation = input("Enter an operation (+, -, *, /): ")
    
    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation. Please enter one of +, -, *, /.")
        continue
    
    second_number = input("Enter the second number: ")
    
    if second_number.lower() == 'exit':
        print("Thank you for using the calculator. Goodbye!")
        break
    
    try:
        second_number = float(second_number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    
    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        if second_number != 0:
            result = first_number / second_number
        else:
            print("Error: Division by zero is not allowed.")
            continue
    
    print(f"The result of {first_number} {operation} {second_number} is: {result}")
