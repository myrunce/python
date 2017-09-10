#multiples part 1

x = 0
while x < 1000:
    x += 1
    if x % 2 != 0:
        print x

#multiples part 2 

x = 5
while x < 1000000:
    if x % 5 == 0:
        print x
        x += 1
    else:
        x += 1

#sumList

randomArr = [1, 2, 5, 10, 255, 3]
arrSum = 0
for element in randomArr:
    arrSum = arrSum + element
print arrSum

#averageList

randomArr = [1, 2, 5, 10, 255, 3]
arrSum = 0
for element in randomArr:
    arrSum = arrSum + element
average = arrSum/len(randomArr)
print average
