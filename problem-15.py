'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

# imagining right = 1, down = 0, the problem becomes generating unique permutations 
# of 1 and 0s 

# https://math.stackexchange.com/questions/1203251/how-many-different-permutations-are-there-of-the-sequence-of-letters-in-mississ 
# ^above site gives the mathematical formula for counting the unique permutations

# attempt 3 

from math import factorial 

print(factorial(40)/(factorial(20)*factorial(20)))

# time complexity: 
# space complexity:
# code length:
# extra comments: there are multiple ways so solve this problem, including pascal's triangle, check Project Euler's comment page!!