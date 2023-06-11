import sys

c = [1, 1, 2, 2, 2, 8]
l = list(sys.stdin.readline().split())
for i in range(len(c)):
    print(c[i] - int(l[i]), end=' ')