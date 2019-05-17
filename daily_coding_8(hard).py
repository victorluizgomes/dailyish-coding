'''
There exists a staircase with N steps, and you can climb up either
1 or 2 steps at a time. Given N, write a function that returns the
number of unique ways you can climb the staircase. The order of the
steps matters.

For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

def stair(n):
    
    return staircase(n + 1)

def staircase(n):
    
    if n == 0 or n == 1:
        return n

    return staircase(n-1) + staircase(n-2)

    # WRONG VERY BAD ATTEMPT
    '''
    if n < 0:
        return 0

    main = []

    i = 0
    new_l = []
    
    while i < n:
        new_l.append(1)
        i += 1

    main.append(new_l)

    # go through each size of list
    i = 0
    while i < n:

        
        size = n - 1
        num_of_twos = 1
        
        j = 0
        while j < size:
            
        
        i += 1

        numTwos = 0

        if n % 2 >= 1:
            
            lowestAmountTwos  = 1

        else:

            new_l.append(2)
            new_l.append(1)
    '''
    

# TESTCASES:
print(stair(4)) # Should output 5
