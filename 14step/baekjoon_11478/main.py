import sys

S = list(sys.stdin.readline().strip())
result = set()
for i in range(1, len(S)+1):
    for j in range(len(S)):
        if j+i > len(S):
            break
        else:
            result.add(''.join(S[j:j+i]))
print(len(result))