import sys

N = int(sys.stdin.readline())
arr = ['ChongChong']

for _ in range(N):
    a, b = sys.stdin.readline().rstrip().split()

    if arr.count(a) or arr.count(b):
        if arr.count(a):
            arr.append(b)
        else:
            arr.append(a)

print(len(set(arr)))