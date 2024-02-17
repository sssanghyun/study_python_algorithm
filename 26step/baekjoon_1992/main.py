import sys

N = int(sys.stdin.readline())
p = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]


# 배열의 시작과 끝 위치, 크기를 받음
def d(x, y, n):
    color = p[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != p[i][j]:
                print('(', end='')
                d(x, y, n // 2)
                d(x, y + n // 2, n // 2)
                d(x + n // 2, y, n // 2)
                d(x + n // 2, y + n // 2, n // 2)
                print(')', end='')
                return
    if color == 0:
        print(0, end='')
    else:
        print(1, end='')


d(0, 0, N)