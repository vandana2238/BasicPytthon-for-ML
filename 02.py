# Q1

# def round_to_two_places(num):
#     """Return the given number rounded to two decimal places. 
    
#     >>> round_to_two_places(3.14159)
#     3.14
#     """
#     return round(num,2)
#     pass

# # Check your answer
# q1.check()

# Q2

# round(356,-2) 
# #output : 400
# round(347,-1)
# #output : 350

# Q3

# def to_smash(total_candies,nfriends = 3):
#     """Return the number of leftover candies that must be smashed after distributing
#     the given number of candies evenly between 3 or given no of friends.
    
#     >>> to_smash(91)
#     1
#     """
#     return total_candies % nfriends

# # Check your answer
# q3.check()

# Q4

# #finding errors

# ruound_to_two_places(9.9999) #NameError

# x = -10
# y = 5
# #Which of the two variables above has the smallest absolute value?
# smallest_abs = min(abs(x, y)) #TypeError
