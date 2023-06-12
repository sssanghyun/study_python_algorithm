import sys


S = sys.stdin.readline().rstrip()

result = {}

for i in range(len(S)):
    try:
        result[S[i].upper()] += 1
    except KeyError:
        result[S[i].upper()] = 1

if len([k for k, v in result.items() if max(result.values()) == v]) > 1:
    print('?')
else:
    print(*[k for k, v in result.items() if max(result.values()) == v])