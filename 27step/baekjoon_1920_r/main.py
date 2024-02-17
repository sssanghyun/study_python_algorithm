# 참고 https://chancoding.tistory.com/44
import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split(' '))))

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split(' ')))


def even(start, end, n):
    if start > end:
        return 0

    half = (start + end) // 2
    if A[half] == n:
        return 1

    if A[half] > n:
        return even(start, half - 1, n)
    else:
        return even(half + 1, end, n)


for i in B:
    print(even(0, N-1, i))