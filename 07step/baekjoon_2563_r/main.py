# 참고 https://velog.io/@zinu/%EB%B0%B1%EC%A4%80-2563-%EC%83%89%EC%A2%85%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2%EC%B0%A8%EC%9B%90%EB%B0%B0%EC%97%B4
import sys

A = [[0 for _ in range(101)]for _ in range(101)]
N = int(sys.stdin.readline())
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())

    for row in range(x, x+10):
        for col in range(y, y+10):
            A[row][col] = 1

result = 0

for i in A:
    result += sum(i)
print(result)