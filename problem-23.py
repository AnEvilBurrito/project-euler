'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and 
it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be 
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers 
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

def proper_divisors(n):
    
    div = [] 
    i = 1 
    while i**2 <= n:
        if n % i == 0: 
            div.append(i)
            if int(n/i) != i and i != 1: 
                div.append(int(n/i))
        i += 1 

    return div  

def abundant(n):
    if sum(proper_divisors(n)) > n:
        return True 
    else:
        return False

abun = {}
i = 1
while i < 28123:
    if abundant(i):
        abun[i] = True
    else: 
        abun[i] = False 
    i += 1

print('Generated abundant numbers < 28123')

def sumOfAbundant(n):
    i = 1 
    while i <= n//2:
        if abun[i] and abun[n-i]:
            # print(i, n-i)
            return True 
        i += 1 

    return False 

nonAbun = []
i = 0 
while i < 28123: 
    if not sumOfAbundant(i): 
        nonAbun.append(i)
    # print('up to', i)
    i += 1 

print(nonAbun)
print(sum(nonAbun))


'''
Time complexity: can be improved, come back to this!!
Space complexity: 
Code length:  
readability: 

comment: 

'''
