# 참고 https://eunhee-programming.tistory.com/101
import sys

N = int(sys.stdin.readline())
M = 2

while N != 1:
    if N % M == 0:
        print(M)
        N = N // M
    else:
        M += 1