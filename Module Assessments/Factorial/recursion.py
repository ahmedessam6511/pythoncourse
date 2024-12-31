def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

       
num = input("Enter a number: ")
if num.isnumeric() and int(num) >= 0:
    print(f"factorial is: {factorial(int(num))}") 
else:
    print("please enter a vaid number!")     