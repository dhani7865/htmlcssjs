number = int(input("Enter a number between 1-10")):
    print("You ntr th numbr", number)



import sys

try:
    num = int(input("Enter a number between 1 - 10: "))

    except ValueError:
        print("Please use numbers only")
        sys.exit() #forces program to stop gracefully after the error
        print("You entered the number", num)
