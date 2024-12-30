first_number = input("Please enter first number:")
second_number = input("Please enter second number:")

if(first_number.isnumeric() and second_number.isnumeric()):
    first_number = int(first_number)
    second_number = int(second_number)
    sum = first_number + second_number
    subtraction = first_number - second_number
    multiplication = first_number * second_number
    division = first_number / second_number
    print("Sum: ", sum, "\nsubtraction: ", subtraction, "\nmultiplication", multiplication,"\ndivision: ",division)
else:
    print("Please enter a valid numbers!")
