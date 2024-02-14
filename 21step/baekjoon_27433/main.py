import sys

def p(n):
    if n <= 1:
        return 1
    else:
        return n * p(n-1)

N = int(sys.stdin.readline())

print(p(N))