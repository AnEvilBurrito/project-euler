'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million
'''

# advanced primality testing 
# https://cp-algorithms.com/algebra/primality_tests.html

# Primality test from wikipedia 
# https://en.wikipedia.org/wiki/Primality_test
# O(sqrt(N)) time complexity 
def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

sum_ = 0 
i = 2
while i < 2000000: 
    if is_prime(i):
        sum_ += i 
        print(i)
    i += 2 

print("sum:", sum_)

'''
Time complexity: 
Space complexity: 
Code length: 
'''
