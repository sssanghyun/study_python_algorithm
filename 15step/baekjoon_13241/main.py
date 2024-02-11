import sys

A, B = map(int, sys.stdin.readline().split())
if min(A, B) == 1:
    print(max(A, B))
else:
    AA, BB = A, B
    while BB:
        AA, BB = BB, AA % BB
    print(int(A * B / AA))