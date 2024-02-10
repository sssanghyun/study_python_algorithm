import sys

N = int(sys.stdin.readline())
arr = [[] for row in range(N)]


for i in range(N):
    age, name = sys.stdin.readline().strip().split()
    arr[i] = list([int(age), name])

arr.sort(key=lambda x: x[0])

for result in arr:
    print(result[0], result[1])