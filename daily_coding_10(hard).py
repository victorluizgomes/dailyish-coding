'''
Given an array of integers and a number k, where 1 <= k <= length
of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3,
we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
'''

def max_k_val(arr, k):

    # simplest looking answer with python
    for i in range(len(arr)):
        if i + k <= len(arr):
            print(max(arr[i:i + k]))

    # TODO: make a O(n) solution

# TESTCASE
max_k_val([10, 5, 2, 7, 8, 7], 3) # should give 10, 7, 8, 8
    
