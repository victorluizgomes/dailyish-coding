'''
Given an array A of non-negative integers, return an array consisting
of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
'''

def sort_by_parity(A):

    even = []
    odd = []
    for i in range(len(A)):
        if A[i] % 2 == 0:
            even.append(A[i])
        else:
            odd.append(A[i])

    return even + odd

    



# TESTCASES
A = [3, 1, 2, 4]
print(sort_by_parity(A))
# should be [2, 4, 3, 1] or [4, 2, 3, 1] or [2, 4, 1, 3] or [4, 2, 1, 3]
