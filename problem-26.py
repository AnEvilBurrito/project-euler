'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

def ld_cycle(n, d=1):
    # n = numerator / d = denominator 
    # cycle finding using concepts from long division 
    all_digits = []
    all_cd = []

    cd = d 
    while True : 

        if cd*10 in all_cd:
            pos = len(all_cd) - 1 - all_cd[::-1].index(cd*10)
            break

        if cd > n:
            cd = cd%n 
        elif cd == 0: 
            return []
        else: 
            cd = cd * 10 
            all_cd.append(cd)
            all_digits.append(cd//n)

        # print(cd)
    # print(all_cd)
    # print(all_digits)
    
    return all_digits[pos:]


all_lengths = []
for x in range(2, 1000+1):
    all_lengths.append(len(ld_cycle(x)))
    # print(x, ld_cycle(x), len(ld_cycle(x)))

import numpy as np 
print(np.argmax(all_lengths)+2) # find the position of max val in all_length, 
# but +2, since python index start at 0 and we began from 2 instead of 1 in the for loop 

print(ld_cycle(983))


'''
Time complexity: 
Space complexity: 
Code length:  
readability: 

comment: 

'''