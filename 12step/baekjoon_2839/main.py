#https://ooyoung.tistory.com/81 참고

import sys

N = int(sys.stdin.readline())

count = 0

while N >= 0:
    if N % 5 == 0:
        count += N // 5
        print(count)
        break
    N -= 3
    count += 1
else:
    print(-1)