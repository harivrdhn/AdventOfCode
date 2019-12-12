low =  123257
high = 647015

def checkVal(digits):
    similarAdj = False
    theDigit = 0
    j = 0
    counter = [0] * 10
    while j < len(digits) - 1:
        if digits[j] > digits[j+1]:
            return False
        else:
            counter[digits[j]] += 1
        j += 1
    counter[digits[-1]] += 1
    for i in counter:
        if i == 2:
            return True
    return False

count = 0
for i in range(low, high):
    digits = [int(x) for x in str(i)]
    if checkVal(digits):
        count += 1
    
print(count)