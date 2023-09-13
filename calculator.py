print(""""""""""Mini calculator""""""""""")

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
while True:
    operation = int(input("Enter a number (1 for addition, 2 for subtraction, 3 for multiplication, 4 for division): "))

    if operation == 1:
        result = num1 + num2
        print("Result:", result)
        break
    elif operation == 2:
        result = num1 - num2
        print("Result:", result)
        break
    elif operation == 3:
        result = num1 * num2
        print("Result:", result)
        break
    elif operation == 4:
        if num2 == 0:
            print("Error: Division by zero")
        else:
            result = num1 / num2
            print("Result:", result)
            break
    else:
        print("Invalid operation choice")
