# 참고 https://happylsm76.tistory.com/entry/%EB%B0%B1%EC%A4%80-2630%EB%B2%88%EC%83%89%EC%A2%85%EC%9D%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0-with-Python
import sys

N = int(sys.stdin.readline())
p = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
w, b = 0, 0


# 배열의 시작과 끝 위치, 크기를 받음
def d(x, y, n):
    global w
    global b
    color = p[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != p[i][j]:
                d(x, y, n // 2)
                d(x, y + n // 2, n // 2)
                d(x + n // 2, y, n // 2)
                d(x + n // 2, y + n // 2, n // 2)
                return
    if color == 0:
        w += 1
    else:
        b += 1


d(0, 0, N)
print(w)
print(b)