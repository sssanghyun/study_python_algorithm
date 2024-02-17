import sys

T = int(sys.stdin.readline())

for _ in range(T):
    result = ''
    a, b = sys.stdin.readline().split()
    for s in b:
        result += s * int(a)
    print(result)