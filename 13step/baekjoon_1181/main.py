import sys

N = int(sys.stdin.readline())
arr = [[] for row in range(N)]
result = []
for i in range(N):
    arr[i] = sys.stdin.readline().strip()

arr.sort()
arr.sort(key=len)

for value in arr:
    if value not in result:
        result.append(value)
        print(value)