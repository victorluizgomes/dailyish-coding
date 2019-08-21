'''
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. 
For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. 
Return True if and only if A can become B after some number of shifts on A.
'''

def rotateString(self, A: str, B: str) -> bool:
        
        if A == B:
            return True
        
        for i in range(0, len(A)):
            
            if A == B:
                return True

            temp = A[len(A) - 1]
            A = A[:len(A) - 1]
            A = temp + A
            
        return False
