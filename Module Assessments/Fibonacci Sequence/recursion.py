def fibonacci(ls, count):
    if count == 1:
        return ls + [(ls[-1]+ls[-2])]
    else:
        ls.append(ls[-1]+ls[-2])
        return fibonacci(ls, count-1)
   


def main():  
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    count = int(input("Enter numbers count: "))
    
    f_seq = [num1,num2]
    fibonacci_seq = fibonacci(f_seq, count)

    print(fibonacci_seq)

main() 