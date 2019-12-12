low =  123257
high = 647015

count = 0
for i in range(low, high):
    digits = [int(x) for x in str(i)]
    similarAdj = False
    tooManySimilarAdj = False
    descending = False
    for j in range(0, len(digits) - 1):
        if digits[j] == digits[j+1]:
            similarAdj = True
        elif digits[j] > digits[j+1]:
            descending = True 
            break
    if similarAdj and not descending:
        count+=1
print(count)