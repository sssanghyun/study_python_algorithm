# https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-19532%EB%B2%88-%EC%88%98%ED%95%99%EC%9D%80-%EB%B9%84%EB%8C%80%EB%A9%B4%EA%B0%95%EC%9D%98%EC%9E%85%EB%8B%88%EB%8B%A4-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython 참고

import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a * i + b * j == c and d * i + e * j == f:
            print(i, j)
            exit(0)