# https://www.hackerrank.com/challenges/diagonal-difference/problem

# 1 2 3
# 4 5 6
# 9 8 9
def diagonalDifference(arr):
    a=0
    b=0
    for i in range(len(arr)):
        a = a + arr[i][i]
        b = b + arr[len(arr)-1-i][i]
    return abs(a-b)

arr = [
    [1,2,3],
    [4,5,6],
    [9,8,9]
]
print(diagonalDifference(arr))