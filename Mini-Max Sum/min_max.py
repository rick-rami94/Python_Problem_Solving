def min_max(arr):
    min_sum,max_sum = sum(sorted(arr)[:-1]), sum(sorted(arr)[1:])
    print(f"The min sum is {min_sum} and the max sum is {max_sum}.")

arr = [4,2,3,5,1]
min_max(arr)