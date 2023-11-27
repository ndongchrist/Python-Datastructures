#How to create a tuple
myTuple = tuple() #using tuple()
myTuple = ('a', 'b', 'c', 'd', 'e')

#traversing a tuple0
for i in myTuple:
    # print(i)
    pass
#searching for an element in a tuple
bool1 = 'e' in myTuple #use in method
# OR
def searchTuple(pTuple, element):
    for i in pTuple:
        if i == element:
            # print('Found')
            pass
        else:
            # print('Not Found') 
            pass

#tupleoperations and functions
newTuple = tuple('tyrth')

myTuple + newTuple #addition
myTuple * 2 #multiplication
myTuple.count('a') #use count for counting elements 
tuple([1, 2, 3]) #converting a list into a couple

#You can't change a single or more elements in a couple, 
#you can delete the entire couple or resign it to new variables 

#methods that cannot be performed on typles
'''
- append()
- insert()
- remove()
- pop()
- clear()
- sort()
- remove()
'''
#you can use the imdex and count() methods
#Both tuples and lists can be nested
