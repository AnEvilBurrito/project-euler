'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K 
text file containing over five-thousand first names, begin by sorting it 
into alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

with open("p022_names.txt", encoding='utf-8') as f:
    content = f.read()
    names = content.split(",")
    names = [n.replace('"','').lower() for n in names]

sortedNames = sorted(names) 

# print(sortedNames)

totalScore = 0 

i = 0 
while i < len(sortedNames): 
    name = sortedNames[i]
    position = i + 1
    score = position * sum([(ord(l) - 96) for l in list(name)])
    totalScore += score 
    i += 1 

print(totalScore)

# print(ord('a') - 96)

'''
Time complexity: ... 
Space complexity: 
Code length:  
readability: list comprehension is easy to code, but hard to read later on 

comment: 

'''
