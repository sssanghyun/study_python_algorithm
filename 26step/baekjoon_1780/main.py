import sys

N = int(sys.stdin.readline())
p = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
a,b,c = 0,0,0

# 배열의 시작과 끝 위치, 크기를 받음
def d(x, y, n):
    global a, b, c
    color = p[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != p[i][j]:
                d(x, y, n // 3)
                d(x, y + n // 3, n // 3)
                d(x, y + n // 3 * 2, n // 3)

                d(x + n // 3, y, n // 3)
                d(x + n // 3, y + n // 3, n // 3)
                d(x + n // 3, y + n // 3 * 2, n // 3)

                d(x + n // 3 * 2, y, n // 3)
                d(x + n // 3 * 2, y + n // 3, n // 3)
                d(x + n // 3 * 2, y + n // 3 * 2, n // 3)
                return
    if color == -1:
        a += 1
    elif color == 0:
        b += 1
    else:
        c += 1

d(0, 0, N)
print(a)
print(b)
print(c)