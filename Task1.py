# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        try:
            # Prompt the user to choose an operation
            choice = int(input("Enter your choice (1/2/3/4/5): "))
            
            if choice == 5:
                print("Exiting the calculator.")
                break
            
            if choice in [1, 2, 3, 4]:
                # Prompt the user for input numbers
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                if choice == 1:
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == 2:
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == 3:
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == 4:
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid choice. Please select a valid option.")
        
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
