import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
result = []
for i in range(M, N + 1):
    if i == 2:
        result.append(2)
        continue
    for j in range(1, i):
        if j == 1:
            continue

        if i % j == 0:
            break
        else:
            if j == i-1:
                result.append(i)
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))