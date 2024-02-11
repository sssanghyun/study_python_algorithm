# 참고 https://lifeofyoori.tistory.com/75

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    if min(A, B) == 1:
        print(max(A, B))
    else:
        AA, BB = A, B
        while BB:
            AA, BB = BB, AA % BB
        print(int(A * B / AA))