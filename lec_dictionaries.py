# Certain execution commands for the dictionaries in python.
purse = dict()
purse['money'] = 51
purse['candy'] = 'yes'
print(purse)
print(purse['money'])

purse['money'] = purse['money'] + 10
print(purse['money'])


# Append the values by providing the key and its value directly. You do not need to use the append function


# Dictionary literals use curly brace and have a key: value pairs

sample = {'chuck' : 1 , 'fred' : 42, 'jan' : 100}

print(sample)

# define empty dictionary 

empty_dict = {}

print(empty_dict)


# Its an error to reference a key in dict if its not available. You will get teh KeyError


# Retrieving list of Keys and Values :


print(list(sample))

print(list(sample.keys()))

print(list(sample.values()))

# items return a tuple 
print(list(sample.items()))


# 

for aaa, bbb in sample.items():

    print(aaa, bbb)