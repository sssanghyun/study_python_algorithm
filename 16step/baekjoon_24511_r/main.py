# 참고 https://velog.io/@yimethan/%EB%B0%B1%EC%A4%80-Python-24511-queuestack

import sys
from collections import deque

N = int(sys.stdin.readline())

# 자료구조 0-> 큐 | 1-> 스택
s = list(map(int, sys.stdin.readline().split()))
# 자료구조 원소
a = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

# 들어갈 원소
b = list(map(int, sys.stdin.readline().split()))

d = deque()

for q in range(N):
    if s[q] == 0:
        d.appendleft(a[q])

for i in range(M):
    d.append(b[i])
    print(d.popleft(), end=' ')