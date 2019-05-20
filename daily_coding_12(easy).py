'''
Given an array of time intervals (start, end) for classroom lectures
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

def rooms(interv):

    # TODO not a finished working solution

    if len(interv) <= 1:
        return len(interv)

    rooms = 1
    for i in range(len(interv)):

        for j in range(i + 1, len(interv)):

            if interv[j][0] >= interv[i][0] and interv[j][0] <= interv[i][1]:
                rooms += 1
                break

            if interv[j][1] >= interv[i][0] and interv[j][1] <= interv[i][1]:
                rooms += 1
                break


    return rooms




# TESTCASES:
print(rooms([(30, 75), (0, 50), (60, 150)])) # should return 2 rooms

# should be 4 rooms
print(rooms([(0, 50), (30, 75), (60, 150), (10, 87), (100, 120), \
             (40, 80), (150, 200)])) 
