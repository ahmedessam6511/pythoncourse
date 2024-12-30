def main():
    start_year = input("Enter the start year: ")
    end_year = input("Enter the End year: ")
    if (start_year.isnumeric() and end_year.isnumeric()):
        if(end_year >= start_year):    
            age = int(end_year) - int(start_year)
            print("Age of the person is ", age, " years")
        else:
            print("Input logical error!")
    else:
        print("Invalid Input!!")

main()