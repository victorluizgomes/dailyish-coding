'''
On election day, a voting machine writes data in the form
(voter_id, candidate_id) to a text file.
Write a program that reads this file as a stream and returns the
top 3 candidates at any given time.

If you find a voter voting more than once, report this as fraud.
'''

def read_votes(filename):

    # holds 3 candidates, and their number of votes
    top_three = [[0, -1], [0, -1], [0, -1]]
    all_candidates = {} # {candidate_id:[#_votes,[voters]], ...}

    votes = open(filename)
    if votes:
        votes = votes.readlines()
        for line in votes: # go through the vote lines
            line = line.strip() # strip trailling whitespace
            line = line.strip('(')
            line = line.strip(')')
            line = line.split(', ')

            # check if that candidate exists in dictionary
            if line[1] not in all_candidates:
                all_candidates[line[1]] = [0, []]

            fraud = False
            # check if the voter has already voted
            for candidate in all_candidates:
                if line[0] in all_candidates[candidate][1]:
                    print("FRAUD REPORT - Voter: " + line[0] +
                      " voted more than once.")
                    fraud = not fraud
                    break                  

            if not fraud:
                # add to the list and add a vote or report voter.
                if line[0] not in all_candidates[line[1]][1]:
                    all_candidates[line[1]][1].append(line[0])
                    all_candidates[line[1]][0] += 1
            

        # goes through candidates in the dictionary and determines the top 3
        for candidate in all_candidates:
            for i in range(len(top_three)):
                if top_three[i][1] < all_candidates[candidate][0]:
                    top_three[i][0] = candidate
                    top_three[i][1] = all_candidates[candidate][0]
                    break

        # print results
        print(top_three)
            

    else:
        print("Not possible to read votes")

            


read_votes('15_file.txt')
# assuming file contents as follows:
'''
(123, 011)
(abc, 011)
(3232, 011)
(210, 092)
(a23, 001)
(abc, 092)
(red, 002)
'''

# gives out output:
'''
FRAUD REPORT - Voter: abc voted more than once.
[['011', 3], ['092', 1], ['001', 1]]
'''
