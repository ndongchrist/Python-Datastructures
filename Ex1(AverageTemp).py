numDays = int(input("How many day's temperature? "))
total = 0
pyArray = []

for i in range(0, numDays):
    nextDay = int(input(f"Day {i+1}'s high temp: "))
    pyArray.append(nextDay)
    total += pyArray[i]

avg = round(total/numDays,2)
print(avg)

above = 0
for i in pyArray:
    if i > avg:
        above += 1

print(str(above) + "are above the avg temp")