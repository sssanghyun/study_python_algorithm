import sys

l = list(i for i in range(1, 31))

for _ in range(28):
    n = int(sys.stdin.readline())
    l[n - 1] = 0

l.sort()
print(l[-2])
print(l[-1])