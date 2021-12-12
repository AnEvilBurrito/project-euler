'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

# Using Euclid's formula from https://en.wikipedia.org/wiki/Pythagorean_triple
# a=m^{2}-n^{2},\ \,b=2mn,\ \,c=m^{2}+n^{2}, m > n > 0

m = 2 

m_max = 1000 
sum_ = 0 

while m < m_max and sum_ <= 1000:

    n = 1
    while n < m: 
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2 
        
        sum_ = a+b+c 
        pro = a*b*c 
        # print(sum_)
        if 1000 % sum_ == 0:
            print("HIT", a,b,c)
            
            mul = 1000 / sum_
            am, bm, cm = a*mul, b*mul, c*mul 
            print(am*bm*cm) 

        n += 1 

    m += 1 



'''
Time complexity: 
Space complexity: 
Code length: 
'''
