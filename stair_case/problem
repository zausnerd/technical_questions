# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

# def staircase(n, obj):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 0
#     if n not in obj:
#         obj[n] = staircase(n - 2, obj) + staircase(n - 1, obj) + staircase(n - 3, obj)
#     return obj[n]

from functools import reduce
def staircase(n, obj, step_types):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n not in obj:
        obj[n] = sum([staircase(n - step, obj, step_types) for step in step_types])
    return obj[n]

        
print(staircase(7, {}, (1, 2, 3)))

