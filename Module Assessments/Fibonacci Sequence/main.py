def main():  
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    n = int(input("Enter numbers count: "))
    f_seq = [num1, num2]
    next_number = num2
    count =  1
    while count <= n :
        count+=1
        next_number = num1+num2
        f_seq.append(next_number)
        num1, num2 = num2, next_number

    print(f_seq)

main() 