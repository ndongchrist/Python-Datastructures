myDict = dict() #declaring a dictionary

#Adding and inserting pairs in a dictionary
myDict = {
    'name': 'Edy',
    'age': 45,
    'address': 'london'
}

myDict['name'] = 'john'

#traversing through a dictionary
def traverseDict(dict):
    for k,v in dict:
        print(k, dict[k])

#finding an element in a dictionary
def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
        else: return 'Not Found'

#deleting and element from the dictionary
    #using pop()
myDict.pop('address')
    #using popitem()
myDict.popitem()
    #using clear() to all pairs
myDict.clear()
    #using del to delete the 
del myDict


myDict = {
    'name': 'Edy',
    'age': 45,
    'address': 'london',
    'education': 'Doctorate'
}

#dictionary methods

dictCopy = myDict.copy() #copy()

newdict = {}.fromkeys([1,2,3], 0) #fromkeys - dict.fromkeys([keys], value)

age = myDict.get('a') #get()

myDict.items()  #items

mykeys = myDict.keys() #keys

myvalues = myDict.values() #values()

setDef = myDict.setdefault('lastname', 'chris') #setdefault()

newdict = {'a': 1, 'b': 2,  'c': 3}
myDict.update(newdict) #update()

#Dictionary Operations

bool1 = 'a' in myDict #in operator

for key in myDict: #fpr operator
    myDict.values()

newdict = {1: False, 2: False}
all(newdict) #checks the boolean values in a dictionary and returns true if all values are true

bool2 = any(newdict) #any

lenght = len(myDict) #len - calculates the number of pairs

newdict = {'e': 1, 'a': 2,  'u': 3, "o":4, 'i': 5}

sortedDict = sorted(newdict, reverse=True) #sorted()

print(sortedDict)


