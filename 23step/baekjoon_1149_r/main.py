# 참고 https://velog.io/@hope1213/%EB%B0%B1%EC%A4%80-1149-RGB%EA%B1%B0%EB%A6%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys

N = int(sys.stdin.readline())
arr = [[0]] * N

for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().split(' ')))

for i in range(1, N):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]

print(min(arr[N-1][0], arr[N-1][1], arr[N-1][2]))