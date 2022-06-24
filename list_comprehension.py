# https://www.hackerrank.com/challenges/list-comprehensions/problem

x = 1
y = 2
a = [ [i,j] for i in range(x+1) for j in range(y+1) if i + j != 3 ]
print(a)
