import sys

input_data = []
xl = []
yl = []
x, y = 0, 0
for _ in range(3):
    input_data = list(map(int, sys.stdin.readline().split()))
    xl.append(input_data[0])
    yl.append(input_data[1])

for i in range(3):
    if xl.count(xl[i]) == 1:
        x = xl[i]
    if yl.count(yl[i]) == 1:
        y = yl[i]
    if x != 0 and y !=0:
        break
print(x, y)