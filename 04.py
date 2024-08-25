# # Q1

# def select_second(L):
#     """Return the second element of the given list. If the list has no second
#     element, return None.
#     """
#     if len(L) < 2:
#         return None
#     return L[1]
# # Check your answer
# q1.check() #Correct

# Q2

# def losing_team_captain(teams):
#     """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
#     from the last listed team
#     """
#     return teams[-1][1]

# # Check your answer
# q2.check() #Correct

# Q3

# def purple_shell(racers):
#     """Given a list of racers, set the first place racer (at the front of the list) to last
#     place and vice versa.
    
#     >>> r = ["Mario", "Bowser", "Luigi"]
#     >>> purple_shell(r)
#     >>> r
#     ["Luigi", "Bowser", "Mario"]
#     """
#     racers[0],racers[-1] = racers[-1],racers[0]

# # Check your answer
# q3.check() #Correct

# Q4

# def fashionably_late(arrivals, name):
#     """Given an ordered list of arrivals to the party and a name, return whether the guest with that
#     name was fashionably late.
#     """
#     order = arrivals.index(name)
#     return (order >= len(arrivals)) / 2 and (order != len(arrivals) - 1)

# # Check your answer
# q5.check() #Correct





