def is_disarium(num):
    digits = str(num)
    total = 0
    for i in range(len(digits)):
        total += int(digits[i]) ** (i + 1)
    return total == num

def game():
    number = int(input("Enter a number: "))
    if is_disarium(number):
        print("Correct! It is a Disarium number 🎉")
    else:
        print("Invalid input ❌ Not a Disarium number")

game()