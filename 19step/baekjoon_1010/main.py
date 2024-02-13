import sys

def p(n):
    if n > 1:
        return n * p(n-1)
    else:
        return 1

T = int(sys.stdin.readline())

for _ in range(T):
    K, N = map(int, sys.stdin.readline().split())
    print(p(N) // p(K) // p(N-K))