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
        return "one thousand"
    elif len(str(n)) == 3:
        base2 = (n // 100)
        base10 = n % 100
        return num2words[base2] + "hundred and" + n2w_base1(base10)
    elif len(str(n)) == 2:
        if n <= 20: 
            return num2words[n]
        else: 
            return n2w_base1(n)
    elif len(str(n)) == 1:
        return num2words[n]

def n2w_base1(n): 
    base0 = n % 10 
    base1 = (n // 10) * 10 
    return num2words[base1] + num2words[base0]

print(n2w(311))