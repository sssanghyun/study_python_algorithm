# 참고 https://shoark7.github.io/programming/algorithm/3-ways-to-get-binomial-coefficients
import sys

def p(n):
    if n > 1:
        return n * p(n-1)
    else:
        return 1

N, K = map(int, sys.stdin.readline().split())

print(p(N) // p(K) // p(N-K))