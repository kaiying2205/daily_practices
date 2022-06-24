# https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true

def compareTriplets(a, b):
    x = 0
    y = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            x = x + 1
        elif b[i] > a[i]:
            y = y + 1
    return [x,y]


print(compareTriplets([5,6,11], [3,6,10]))