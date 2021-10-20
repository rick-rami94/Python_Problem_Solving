def plus_minus(arr):
    pos,neg,z = 0,0,0
    for i in arr:
        if i > 0:
            pos+=1
        elif i < 0:
            neg+=1
        else:
            z+=1
    print(f"This array has {pos} positive numbers, {neg} negative numbers, and {z} zeros.")

arr = [-1,-2,0,3,1,0,-19]
plus_minus(arr)