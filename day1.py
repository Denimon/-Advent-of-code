

def calculateFuel(val):
    if int(val) <= 0:
        return 0

    return val + calculateFuel(((int(val)//3) - 2))


file = open('dayOneInput.txt', 'r')
sum = 0
listOfValues = []


for row in file:
    listOfValues.append((int(row)//3) - 2)
    
    
for val in listOfValues:
    sum += calculateFuel(val)


print(sum)
