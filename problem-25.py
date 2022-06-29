'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''



t1 = 1
t2 = 2 

index = 3 
i = 0
max_steps = 1000000
while i < max_steps:
    prev_t2 = t2 
    t2 = t1 + t2 # t2 = fib 
    t1 = prev_t2
    
    index += 1 
    # print(t2, index)
    if len(str(t2)) == 1000:
        print(t2, index)
        break
    i += 1 
    



'''
Time complexity: 
Space complexity: 
Code length:  
readability: 

comment: 

'''