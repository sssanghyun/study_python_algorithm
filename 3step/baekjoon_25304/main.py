result = 0
X = int(input())
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    result += a * b

if not X == result:
    print('No')
else:
    print('Yes')