'''
Extract content from a .txt file 
'''

f = open('numbers-8.txt', 'r')
content = f.read()
n = content.split("\n")
c = "".join(n)
f.close()

# print(c) 
# we can use the 'c' variable to call the numbers as a string 

# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.

# print(len(c)) 

largest = 0 
i = 12 
while i < len(c):

    short = c[i-12:i+1]

    if "0" in short: 
        skip_digits = short.index('0')
        print(short, "SKIP", skip_digits)
        i += skip_digits
    else:
        number = 1 
        for s in short: 
            number = number * int(s) 

        if number > largest:
            largest = number

        print(short) 

    i += 1 

print("largest product", largest)

'''
Time complexity: 
Space complexity: 
Code length: 
'''
