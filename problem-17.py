'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero', 1000: 'One thousand'}


def n2w(n):
    if n < 1 or n > 1000:
        return None 
    if len(str(n)) == 4: 
        return "OneThousand"
    elif len(str(n)) == 3:
        base2 = (n // 100)
        base10 = n % 100
        if base10 == 0: 
            return num2words[base2] + "Hundred"
        else: 
            return num2words[base2] + "HundredAnd" + n2w_base1(base10)
    elif len(str(n)) == 2:
        return n2w_base1(n)
    elif len(str(n)) == 1:
        return num2words[n]

def n2w_base1(n): 
    if n <= 20: 
        return num2words[n] 
    else: 
        base0 = n % 10 
        base1 = (n // 10) * 10 
        if base0 == 0: 
            return num2words[base1]
        else: 
            return num2words[base1] + num2words[base0]

# print(n2w(40))

final_length = 0
for i in range(1,1001):
    final_length += len(n2w(i)) 
    print(i, n2w(i), final_length)

print(final_length)


'''
Time complexity: ... 
Space complexity: 
Code length:  
readability: probably needs improvement 

comment: very annoying problem to debug. Better debugging methods?

'''
