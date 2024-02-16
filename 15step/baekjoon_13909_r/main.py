# 참고 https://velog.io/@jannie526/%EB%B0%B1%EC%A4%80-13909%EB%B2%88
import sys

N = int(sys.stdin.readline())
i = 1
count = 0

while i * i <= N:
    i += 1
    count += 1

print(count)