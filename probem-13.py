'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
'''

f = open('numbers-13.txt', 'r')
content = f.read()
n = content.split("\n")
f.close()

n = [int(i) for i in n]
sum_ = sum(n) 

print(sum_)

'''
Time complexity: 
Space complexity: 
Code length: 

extra comment: ???
probably not a programmically challenging question 
'''
