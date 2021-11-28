# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

x = []

i = 1
while i < 1000:
    
    # x only takes in natural numbers that is fully divisible by 5 or 3 

    if i % 5 == 0:
        x.append(i)

    elif i % 3 == 0: 
        x.append(i)

    i += 1  

x = list(set(x)) # removing duplicates in the list x 
print(sum(x))

# time complexity: O(N), N = amount of natural numbers iterated, e.g. 1000
# space complexity: O(N/3 + N/5) == O(N), assuming if every member can be divisible by 3 or 5, then 1/3 + 1/5 of digits will be retained 
# code length: 10, this can be improved (maybe using other languages too!)