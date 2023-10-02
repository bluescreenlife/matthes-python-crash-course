run = True

while run:
    try:
        num1 = int(input("Enter a number (enter q to quit): "))
    
        if num1 == "q":
            break
        else:
            pass

        num2 = int(input("Enter a number to add (enter q to quit): "))

        if num2 == "q":
            break
        else:
            total = num1 + num2

    except ValueError:
        print("Please enter only numbers and try again.")

    try:
        print(f"The total is: {total}")
    except NameError:
        print("Cannot print total due to user error.")

    again = input("Add again? (y/n): ")
    if again == "n":
        run = False
    else:
        pass

