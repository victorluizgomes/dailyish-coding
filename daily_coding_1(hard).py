'''
Given an array of integers, return a new array such that each element
at index i of the new array is the product of all the numbers in the
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
the expected output would be [2, 3, 6].
'''

def product_all(arr):
    '''
    arr: a list of integers
    '''

    # O(n) solution
    # Algo:
    '''
    1) Construct a temporary array left[] such that left[i] contains
        product of all elements on left of arr[i] excluding arr[i].
    2) Construct another temporary array right[] such that right[i]
        contains product of all elements on on right of arr[i] excluding arr[i].
    3) To get prod[], multiply left[] and right[].
    '''
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr
    
    left = [0] * len(arr)
    right = [0] * len(arr)
    new_arr = [0] * len(arr)

    left[0] = 1
    right[len(arr) - 1] = 1

    for i in range(1, len(arr)):
        left[i] = arr[i - 1] * left[i - 1]

    for j in range(len(arr) - 2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]

    for i in range(len(arr)):
        new_arr[i] = left[i] * right[i]

    return new_arr
    
    # SUBOPTIMAL working solution below O(n^2)
    '''
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr

    new_arr = [0] * len(arr)

    i = 0
    while i < len(arr):
        mult = 1
        j = 0
        
        while j < len(arr):
            if j != i:
                mult = mult * arr[j]
            j += 1
            
        new_arr[i] = mult
        i += 1
        
    return new_arr
    '''
    

# TESTCASES
result = product_all([1, 2, 3, 4, 5])
print(result) # expected: [120, 60, 40, 30, 24]

result = product_all([3, 2, 1])
print(result) # expected: [2, 3, 6]

result = product_all([10, 3, 5, 6, 2])
print(result) # expected: [180, 600, 360, 300, 900]
