import random
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j>= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key


def print_list(arr):
    for i in  arr:
        print(i, end=" ")
    print()

if __name__ == "__main__":
    nums = []
    for i in range(10):
        nums.append(random.randint(0,100))
        i+=1
    print("Before Sorting:  ", end=" ")
    print_list(nums)
    insertion_sort(nums) 
    print("After merge sort:" , end=" ")
    print_list(nums)