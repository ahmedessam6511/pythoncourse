def main():
    num = input("Enter a number: ")
    factorial = 1
    previous = 0
    if num.isnumeric():
        factorial = int(num)
        if num == 0 or num == 1:
            factorial = 1
        else:
            previous = factorial-1
            while previous > 1:
                factorial = factorial * previous
                previous -= 1
        print(f"factorial: {factorial}") 
    else:
        print("please enter a vaid number!")   

    

main()