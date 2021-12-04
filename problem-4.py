# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# Intuition: Start from largest.. 999 x 999, then iterate down to 998 * 999, 998 * 998
# then. 997 * 999... and so on. 
# in the form of A * B 

# palindrome check: convert digit to string, invert it, check if equal 

def isPalindrome(d: int):
    s = str(d) 
    inverted_s = s[::-1]  # [::-1] inverses the string 
    if s == inverted_s: 
        return True 
    else:
        return False 


# imagine a NxN multiplication table (best to visualise one somehow)
# let's call the horizontal numbers A and verticals B   
# then, we traverse the bottom triangle side of the table 
# first, the largest multiple is A x B when A = 999 and B = 999  

N = 999 
A = N
B = N
stopLoop = False
while A >= 1 and B >= 1 and stopLoop == False: 

    a = A 
    b = B 
    while a >= 1 and b <= N: 
        ans = a * b 

        # print(a,b)
        
        if isPalindrome(ans):
            print(a, b, ans)
            stopLoop = True # break the first loop 
            break # break the smaller loop

        
        a -= 1 
        b += 1


    if A == B: 
        A -= 1 
    else:
        B -= 1 



# time complexity: 
# space complexity: 
# code length: 11, this can be improved (maybe using other languages too!)
