'''
str1 = list(input().strip().split())
str1 = [int(i.strip(",")) for i in str1]
sum = 0
l2 = []
for i in range(len(str1)-1):
    
    if str1[i] > str1[i+1] or i==len(str1)-1:
        sum += str1[i]
        l2.append(sum)
        sum = 0
    else:
        sum += str1[i]

print(max(l2))
'''
'''2, 202, 2, 3, 200, 4, 5'''

# count the frequency of character and print the mostfrequent character
text = "geeaakss" 
all_freq = {}
for i in text:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
        
m = (max(all_freq.values())) #max value()

l1 = [name for name, number in all_freq.items() if number == m]

for i in sorted(l1):
    print(i,end=",")

print(max(all_freq, key=all_freq.get)) #print 1st max in the dictionary

