# 참고 https://itadventure.tistory.com/158
import sys

N = int(sys.stdin.readline())
find = False
start = 0
if N-(len(str(N))*9) > 0:
    start = N-(len(str(N))*9)

for i in range(start, N):
    str_i = str(i)
    sum_str = 0
    for j in range(len(str_i)):
        sum_str += int(str_i[j])

    if i + sum_str == N:
        print(i)
        find = True
        break

if not find:
    print(0)