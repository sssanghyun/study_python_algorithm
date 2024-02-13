import sys

N = int(sys.stdin.readline())

arr = []
count = 0

for _ in range(N):
    chat = sys.stdin.readline().strip()

    if chat == 'ENTER':
        if len(arr):
            s = set(arr)
            count += len(s)
        arr = []
    else:
        arr.append(chat)

if len(arr):
    s = set(arr)
    count += len(s)

print(count)