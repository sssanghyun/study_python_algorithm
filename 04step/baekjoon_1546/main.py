import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

max = max(l)

for i in range(len(l)):
    l[i] = l[i] / max * 100

print(sum(l) / len(l))