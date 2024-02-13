import sys

def p(n):
    if n > 1:
        return n * p(n-1)
    else:
        return 1

N = int(sys.stdin.readline())

print(p(N))