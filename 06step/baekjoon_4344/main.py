import sys

C = int(sys.stdin.readline())

for _ in range(C):
    N = list(map(int, sys.stdin.readline().split()))
    N = N[1:]
    avg = sum(N) / len(N)
    count = 0
    for n in N:
        if n > avg:
            count += 1
    print(format(count / len(N) * 100, ".3f"), end='%\n')
