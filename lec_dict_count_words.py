counts ={}
names = ['csev','cwen','csev','zqian','cwen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)


# Use the get method which returns 1 if found else 0 if not found. Can be used to create a dictionary 
# for identifying and getting countds
count1 ={}
for name in names:
    count1[name] = counts.get(name,0) +1

print(counts)



# counting words in a text

counts3 ={}
print('Enter a line of text :')

line = input('')

words = line.split()

print('words:', words)

print('counting:')
for word in words:
    counts3[word] = counts3.get(word,0) +1
print('Counts', counts3)



# Python knows number of records in a item 
for key in counts3:
    print(key, counts3[key])

