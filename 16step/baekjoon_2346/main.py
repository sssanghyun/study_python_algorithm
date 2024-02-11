import sys
from collections import deque

N = int(sys.stdin.readline())
d = deque([i for i in range(1, N+1)])
a = list(map(int, sys.stdin.readline().split()))

b = d.popleft()
print(b, end=' ')
while d:
    if a[b-1] < 0:
        # 음수
        for j in range(abs(a[b-1])):
            if j == abs(a[b-1]) - 1:
                b = d.pop()
                print(b, end=' ')
            else:
                d.appendleft(d.pop())
    else:
        # 양수
        for j in range(a[b-1]):
            if j == a[b-1] - 1:
                b = d.popleft()
                print(b, end=' ')
            else:
                d.append(d.popleft())