'''
Given an array of integers, find the first missing positive integer
in linear time and constant space. In other words, find the lowest
positive integer that does not exist in the array. The array can contain
duplicates and negative numbers as well.

TODO: sorting is O(n log n) not linear time
'''
def first_miss(arr):
    '''
    arr: array/list of integers
    '''
    lowest = 1
    arr.sort()
    first_one = True
    
    for i in range(len(arr) - 1):
        if arr[i] <= 0:
            continue

        if arr[i] == 1 and first_one:
            first_one = False
            
        elif first_one:
            return 1

        if not first_one and arr[i] + 1 != arr[i + 1]:
            return arr[i] + 1


    return arr[len(arr) - 1] + 1

# TESTCASES:
result = first_miss([3,4,-1,1])
print(result) # should be 2

result = first_miss([1,2,0])
print(result)

result = first_miss([2, 3, -7, 6, 8, 1, -10, 15])
print(result)
