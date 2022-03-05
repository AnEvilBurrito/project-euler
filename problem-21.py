'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

# finding proper divisors in O(sqrt(n)) time in necessary for an efficient solution 

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

# print(sum(sorted(proper_divisors(284))))

def d(n):
    # d is defined within the problem 
    return sum(proper_divisors(n))

# print(d(25))

# find amicable numbers under 10000... 

ami = []

i = 1 
while i < 10000:
    a,b = i, d(i) 

    if d(a) == b and d(b) == a and a != b: 
        ami.append(a)
    i += 1 

print(sum(ami))


'''
Time complexity: ... 
Space complexity: 
Code length:  
readability:

comment: 

'''