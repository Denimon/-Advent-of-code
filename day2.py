

def part1(num1, num2, val):

    val[1] = num1
    val[2] = num2
    i = 0
    while i < len(val):

        firstIndexToCalculate = val[i+1]
        secondIndexToCalculate = val[i+2]
        answerIndex = val[i+3]

        if val[i] == 1:
            val[answerIndex] = val[firstIndexToCalculate] + val[secondIndexToCalculate]

        if val[i] == 2:
            val[answerIndex] = val[firstIndexToCalculate] * val[secondIndexToCalculate]

        if val[i] == 99:
            break

        i += 4

    return val[0]



f = open('dayTwoInput.txt','r')
valuesFromFile = [ int(x) for x in f.read().split(",") ]

#part1
print(part1(12,2,valuesFromFile[:]))


for i in range(100):
    for j in range(100):
            
        if part1(i,j,valuesFromFile[:]) == 19690720:
            print(100*i+j)

f.close()