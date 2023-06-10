import sys

N = 42
l = set()

for _ in range(10):
    n = int(sys.stdin.readline())
    l.add(n%N)

print(len(l))