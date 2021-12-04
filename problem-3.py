# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# Implemented by Triptych on 
# https://stackoverflow.com/questions/23287/algorithm-to-find-largest-prime-factor-of-a-number
# This is an O(Sqrt(N)) time method 

def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1:
                factors.append(n)
            break
    return factors


pfs = prime_factors(600851475143)
largest_prime_factor = max(pfs)  # The largest element in the prime factor list
print(largest_prime_factor)

# time complexity: O(Sqrt(N))
# space complexity: O(Sqrt(N)), loop maximally bounded by d or sqrt(N) 
# code length: 11, this can be improved (maybe using other languages too!)
