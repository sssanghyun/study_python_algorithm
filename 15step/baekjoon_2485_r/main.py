# 참고 https://deok2kim.tistory.com/329

import sys
from math import gcd

N = int(sys.stdin.readline())
B = [[] for _ in range(N-1)]
a = int(sys.stdin.readline())
for i in range(N-1):
    b = int(sys.stdin.readline())
    B[i] = b - a
    a = b
C = list(set(B))
g = C[0]

for i in range(1, len(C)):
    g = gcd(g, C[i])
count = 0
for i in B:
    count += i//g -1

print(count)