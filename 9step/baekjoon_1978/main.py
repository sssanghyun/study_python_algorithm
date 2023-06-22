import sys

N = int(sys.stdin.readline())
count = 0
indata = []

indata = list(map(int, sys.stdin.readline().split()))
for i in indata:
    if i == 2:
        count += 1
        continue
    for j in range(2, i):
        if i % j == 0:
            break
        else:
            if j == i - 1:
                count += 1
print(count)