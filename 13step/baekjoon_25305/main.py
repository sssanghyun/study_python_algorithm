import sys

N, k = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse=True)

print(arr[k-1])