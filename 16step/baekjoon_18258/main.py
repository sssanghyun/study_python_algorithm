import sys
from collections import deque

N = int(sys.stdin.readline())
d = deque()
for i in range(N):
    c = sys.stdin.readline().strip()

    if c[:4] == 'push':
        d.append(int(c[5:]))
    elif c == 'pop':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif c == 'size':
        print(len(d))
    elif c == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif c == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif c == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])