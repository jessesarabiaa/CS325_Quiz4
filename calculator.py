def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Add multiplication function here

# Add division function here

print("Quiz 4 Calculator")
print("Select operation:")
print("+ Add")
print("- Subtract")
print("* Multiply")
print("/ Divide")

choice = input("Enter choice (+,-,*,/): ")

if choice in ('+', '-', '*', '/'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '+':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '-':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '*':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '/':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input")