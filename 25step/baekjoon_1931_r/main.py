# 참고 https://suri78.tistory.com/26
import sys

N = int(sys.stdin.readline())
t = [[0, 0] for _ in range(N)]

for i in range(N):
    s, e = map(int, sys.stdin.readline().split(' '))
    t[i][0] = s
    t[i][1] = e

t.sort(key=lambda x: (x[1], x[0]))

count = 1
end_time = t[0][1]
for i in range(1, N):
    if end_time <= t[i][0]:
        end_time = t[i][1]
        count += 1

print(count)