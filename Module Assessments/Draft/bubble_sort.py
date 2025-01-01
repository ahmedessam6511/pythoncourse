import random 

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if(swapped == False):
            break        

if __name__ == "__main__":
    nums = []
    for i in range(10):
        nums.append(random.randint(0,100))
        i+=1
    print("Before Sorting: "+ str(nums))
    bubble_sort(nums) 
    print("After Sorting:  " + str(nums))
