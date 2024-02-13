import sys

N = int(sys.stdin.readline())
arr = [0 for _ in range(N)]
c = [0 for _ in range(-4000, 4001)]
sum = 0
min = 4000
max = -4000
c_max = -4000

for i in range(N):
    arr[i] = int(sys.stdin.readline())
    sum += arr[i]
    c[arr[i]] += 1
    if c[arr[i]] > c_max:
        c_max = c[arr[i]]
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]

arr.sort()

arr_c = []
for i in range(-4000, 4001):
    if c[i] == c_max:
        arr_c.append(i)

arr_c.sort()

print(round(sum / N))
print(arr[N//2])
if len(arr_c) <= 1:
    print(arr_c[0])
else:
    print(arr_c[1])
print(arr[-1] - arr[0])