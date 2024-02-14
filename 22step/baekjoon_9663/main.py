# 참고 https://seongonion.tistory.com/103
import sys

N = int(sys.stdin.readline())
# 1차원 배열로 인덱스가 행의 값이되고 값이 열의 값이됨
# 1,2 => row[1 -1] == 2
row = [0] * N
count = 0

# x는 깊이
def is_promising(x):
    for i in range(x):
        # row[x]의 열 값과 row[0~x]까지 중 열값이 같은게 있으면 같은 열이기 때문에 False
        # 열값 뺀 값과 행값 뺀 값이 같으면 대각선에 있기 때문에 False
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True

def n_queens(x):
    global count
    # 깊이가 입력받은 N과 같아지면 유망한 값으로 N개가 채워졌기 때문에 count++
    if x == N:
        count += 1
        return
    else:
        for i in range(N):
            row[x] = i
            # 유망한 것만 다음재귀를 시작한다.
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(count)