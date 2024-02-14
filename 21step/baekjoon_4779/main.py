# 참고 https://edder773.tistory.com/209
import sys

def c(index, n):
    if n == 0:
        return
    for i in range(index + 3 ** (n-1), index + 3 ** (n-1) * 2):
        arr[i] = ' '
    c(index, n-1)
    c(index + 3 ** (n-1) * 2, n-1)

while True:
    try:
        N = int(sys.stdin.readline())
        arr = ['-' for _ in range(3 ** N)]
        c(0, N)
        print(''.join(arr))
    except:
        break