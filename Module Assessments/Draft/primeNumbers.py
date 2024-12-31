num = input("Enter the end number: ")
prime_nums = []
if num.isnumeric() and int(num) >= 2:
    start_num = 2
    while start_num <= int(num):
        isPrime = True
        for i in range(2, start_num):
            if start_num%i == 0:
                isPrime = False
                break
        if isPrime:
            prime_nums.append(start_num)
        start_num +=1 
else:
    print("please enter a vaid number!")    


print(prime_nums)