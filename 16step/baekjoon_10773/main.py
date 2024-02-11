import sys

K = int(sys.stdin.readline())
s = []

for _ in range(K):
    a = int(sys.stdin.readline())
    if a == 0 and len(s) != 0:
        s.pop()
    else:
        s.append(a)

result = 0
for i in s:
    result += i
print(result)