import sys

N = int(sys.stdin.readline())
s = []
for i in range(N):
    n = sys.stdin.readline().strip()

    if len(n) == 1:
        n = int(n)
    else:
        n, m = map(int, n.split())

    if n == 1:
        s.append(m)
    elif n == 2:
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())
    elif n == 3:
        print(len(s))
    elif n == 4:
        if len(s) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])
