# The sum of the squares of the first ten natural numbers is,

# The square of the sum of the first ten natural numbers is, 385

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

N = 100

# compute sum square

sum_square = 0
total = 0

i = 1 
while i <= N:
    sum_square += (i**2)
    total += i 
    i += 1 

# compute sum square
square_sum = total**2 
diff = abs(square_sum - sum_square)

print(diff)

# time complexity;
# space complexity;
# code length; 
