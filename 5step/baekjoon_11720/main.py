import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
result = 0
for i in range(len(S)):
    result += int(S[i])

print(result)