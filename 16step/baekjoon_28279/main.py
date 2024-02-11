import sys
from collections import deque

N = int(sys.stdin.readline())
d = deque()

for i in range(N):
    a = sys.stdin.readline().strip()

    if a[0] == '1':
        d.appendleft(a.split()[1])
    elif a[0] == '2':
        d.append(a.split()[1])
    elif a == '3':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif a == '4':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif a == '5':
        print(len(d))
    elif a == '6':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif a == '7':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif a == '8':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])