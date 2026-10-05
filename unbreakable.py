def safe_input():
    try:
        number = int(input("Enter a whole number: "))
        print("You entered:", number)
    except ValueError:
        print("Invalid input. Please enter a whole number.")


safe_input()
