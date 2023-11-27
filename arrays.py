#creating an array
from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.3, 1.5, 1.6])

#inserting an element into an array
arr1.insert(0, 0)

#traversing an array
def traversingArr():
    for i in arr1:
        # print(i)
        pass

#accessing an element in an array
def accessElement(array, index):
    if index >= len(arr1):
        print("Index Error")
    else:
        print(array[index])


#seraching for an element
def searchArr(array, value):
    for i in array:
        if value == array[i]:
            return array.index(value)
        else:
            return "Not Found"
        
#removing an element
arr1.remove(0)

print(arr1)