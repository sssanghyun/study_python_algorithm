import sys

T = int(sys.stdin.readline())
p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90

for _ in range(T):
    N = int(sys.stdin.readline())

    if N > 10:
        for i in range(11, N+1):
            p[i] = p[i-1] + p[i-5]
    print(p[N])