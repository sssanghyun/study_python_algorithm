import sys

A = list()
max = 0
a, b = 0, 0
for i in range(9):
    A.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        if A[i][j] >= max:
            max = A[i][j]
            a = i+1
            b = j+1

print(max, end=' \n')
print(f'{a} {b}')