import math 
import csv

with open("data2.csv", newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]

def mean(data):
    length = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/length
    return mean

squareList = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squareList.append(a)

# Getting the sum

sum = 0
for x in squareList:
    sum += x

result = sum / len(data) - 1    

standardDeviation = math.sqrt(result)

print(standardDeviation)