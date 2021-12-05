# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# an intuitive approach is to test primality for every single number until we reach
# the number that is the 10001st prime. 

# the faster the primality test, the better this approach becomes. 
# here, we borrow the naive O(sqrt) approach on wikipedia
# https://en.wikipedia.org/wiki/Primality_test#

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

p = 2
counter = 0 
it = 10001
while counter < it: 
    if is_prime(p): 
        counter += 1
        if counter == it:
            break

    p += 1

print(p)

# time complexity;
# space complexity;
# code length; 
