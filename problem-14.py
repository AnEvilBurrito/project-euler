'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem)
, it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
---

This problem can definitely be solved by brute force. However, would we want to solve it that way? 

naive approach: 
- for each number between 1 to 1000000, simulate the collatz sequence until it reaches 1 
- find the longest sequence amongst all sequences 
- we can achieve o(1) space complexity by eliminating storage of sequences 

dynamic programming approach: 
- for each number between 1 to 1000000, simulate the collatz sequence 
- if it jumps to a previously known number, i.e. 13, since we already know its length (10), 
we can reduce the amount of computation needed 

- we can achieve O(n) space complexity by eliminating storage of the sequences
- alternatively, using dict can store sequences beyond n but uses more space 
'''

all_length = [0] * 1000001 

for i in range(1, 1000001):
    this_length = 0
    n = i 
    while n != 1:
        # print(n)
        if n <= 1000000: 
            if all_length[n] != 0:
                this_length += all_length[n]
                n = 1 
            else: 
                n = n // 2 if n % 2 == 0 else 3*n + 1 
                this_length += 1
        else:
            n = n // 2 if n % 2 == 0 else 3*n + 1
            this_length += 1

    all_length[i] = this_length
    # print(i, this_length)

print(all_length.index(max(all_length)))


'''
Time complexity: ? it is unknown how long collatz sequences take, but a useful reference: 
https://blog.revolutionanalytics.com/2014/04/a-look-a-r-vectorization-through-the-collatz-conjecture.html
Space complexity: O(N) where n = collatz number limit 
Code length: compact 

comment: time complexity hard to calcualte 

'''
