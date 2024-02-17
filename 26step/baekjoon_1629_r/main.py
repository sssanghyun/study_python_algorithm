# 참고 https://velog.io/@grace0st/%EA%B3%B1%EC%85%88-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys

A, B, C = map(int, sys.stdin.readline().split(' '))

def f(a, b):
    if b == 1:
        return a % C

    if b % 2 == 0:
        return f(a, b // 2) ** 2 % C
    else:
        return f(a, b // 2) ** 2 * a % C


print(f(A, B))