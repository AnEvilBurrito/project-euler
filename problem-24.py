'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

'''
https://cusack.hope.edu/Tutorials/PermsAndCombs/?page=section4_7

has the following solution: 

NextPermutation(a1a2...an)
{
    j = n - 1;
    while (a[j] > a [j+1])
    {
          j--;
    }
    k = n;
    while (a[j] > a[k])
    {
          k--;
    }
    Swap(a[j],a[k]);
    r = n;
    s = j + 1;
    while (r > s)
    {
         Swap(a[r],a[s]);
         r--;
         s++;
    }
}

'''

def nextLex(s):
    s = list(s)
    n = len(s) - 1 # last index  
    j = n - 1
    while int(s[j]) > int(s[j+1]):
        j -= 1 

    k = n
    while int(s[j]) > int(s[k]): 
        k -= 1 

    s[j], s[k] = s[k], s[j]
    r = n
    t = j + 1 
    while r > t: 
        s[r], s[t] = s[t], s[r]
        r -= 1
        t += 1

    return ''.join(s)
    
s = "0123456789"
print(s)
i = 2
while i <= 1000000:
    s = nextLex(s)
    i += 1

print(s, i)
    
# test = "1234" 
# t = list(test)
# t[1], t[2] = t[2], t[1]
# t = ''.join(test)

# print(t)

'''
Time complexity: 
Space complexity: 
Code length:  
readability: 

comment: I actually didn't read this algorithm... need to read 

'''
