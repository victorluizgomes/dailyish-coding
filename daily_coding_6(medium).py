'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be
decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example,
'001' is not allowed.
'''

import string

# TODO: Incomplete

def decode_message(code):
    '''
    code: a string with the code to be decoded
    '''

    decode = {}
    count = 1
    for i in string.ascii_lowercase:
        decode[str(count)] = i
        count += 1

    decoded = []
    possible = ''

    for i in code:
        if i in decode:
            possible += decode[i]

    print(possible)

    return len(decoded)

# TESTCASES
print(decode_message('111')) # should return 3
    
