#3.	Write a program that prompts the user to enter a number within the range of 1 – 10. The program should display the Roman numeral version of that number. If the number is outside the range of 1 – 10, the program should display an error message.

user_input = int(input("Enter a number between 1 and 10:"))
if user_input < 1 or user_input >10:
    print("Error: The number you have entered is not within the 1-10 range.")
else: 
    if user_input < 4:
        print("I" * user_input)
    elif user_input == 4:
        print("IV")
    elif user_input == 5:
        print("V")
    elif user_input < 9:
        print("V" + "I" *  user_input)
    elif user_input == 9:
        print("IX")
    else:
        print("X")
