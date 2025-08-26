def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

print("\n=== Simple Calculator ===")
num1 = get_number("Enter first number: ")
num2 = get_number("Enter second number: ")

print("\nChoose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

print("\n=== Result ===")
if choice == "1":
    print(f"{num1} + {num2} = {num1 + num2}")
elif choice == "2":
    print(f"{num1} - {num2} = {num1 - num2}")
elif choice == "3":
    print(f"{num1} * {num2} = {num1 * num2}")
elif choice == "4":
    if num2 == 0:
        print("Error: Division by zero not allowed!")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Invalid choice! Please select 1, 2, 3, or 4.")
