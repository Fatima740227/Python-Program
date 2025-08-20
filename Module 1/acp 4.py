def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    choice = input("Enter choice: ")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == '1':
        result = add(a, b)
    elif choice == '2':
        result = subtract(a, b)
    else:
        print("Invalid choice")
        return

    print("Final Answer:", result)

main()