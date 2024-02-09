import sys

M, N = map(int, sys.stdin.readline().split())
arr = [[0 for col in range(N)] for row in range(M)]
result = sys.maxsize
for i in range(M):
    arr[i] = list(sys.stdin.readline().strip())

for i in range(M-7):
    for j in range(N-7):
        change = 0
        change1 = 0
        for x in range(8):
            for y in range(8):
                if x % 2 == 0:
                    # x열 짝수
                    if y % 2 == 0:
                        # y열 짝수
                        if arr[i+x][j+y] != 'W':
                            change = change + 1
                        else:
                            change1 = change1 + 1
                    else:
                        # y열 홀수
                        if arr[i+x][j+y] == 'W':
                            change = change + 1
                        else:
                            change1 = change1 + 1
                else:
                    # x열 홀수
                    if y % 2 == 0:
                        # y열 짝수
                        if arr[i+x][j+y] == 'W':
                            change = change + 1
                        else:
                            change1 = change1 + 1
                    else:
                        # y열 홀수
                        if arr[i+x][j+y] != 'W':
                            change = change + 1
                        else:
                            change1 = change1 + 1
        if result >= change or result >= change1:
            result = min(change, change1)
print(result)