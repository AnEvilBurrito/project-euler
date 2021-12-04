# all primes must be factors 

base = 2*3*5*7*11*13*17*19
print(base)

# try the smallest increments of primes

ans = base * 2 * 3 * 2 * 2 
print("answer:",ans) 

print("Visual Checker")
i = 1 
while i < 20:
    if ans % i != 0: 
        print(i, ans % i)
    i += 1 
    
    
