'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

import math 

def divisors_count(n):

    # search only up to sqrt(n) is sufficient 

    divisors = 0 

    i = 1 
    while i*i <= n:
        if n % i == 0: 
            divisors += 1 
            
        i += 1 

    divisors *= 2 
    
    if (i-1)**2 == n:
        divisors -= 1  

    return divisors 


# triangle numbers are simply numbers of incrementing the addition by 1 
# i.e. 1, 1+2, 1+2+3.. 

max_div = 0 
tri = 1 
inc = 2 
while max_div < 500: 
    max_div = divisors_count(tri)
    print(tri, max_div)
    if max_div > 500: 
        break 
    tri += inc 
    inc += 1 

'''
Time complexity: O(sqrt(n)*n)
Space complexity: no storage i.e. O(1)
Code length: long 

comment: it is certain that more efficient algorithms or more elegant coding styles exist for this problem 

'''