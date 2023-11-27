# Two Dimensional Array
twoDArray = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#Inserion in 02 D - Arrays
#use the insert() numpy method to perform this action

numOfDays = int(input("How many day's temperature -> "))
array = []

for i in range(numOfDays):
    value = int(input(f"Day {i + 1}'s high tenperature? "))
    array.append(value)
average = sum(array)/len(array)
print(average)

aboveList = 0
for i in array:
    if i > average:
        aboveList += 1
    else: 
        pass
print(f"{aboveList}'s above average")
