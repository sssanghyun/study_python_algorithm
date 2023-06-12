import sys

S = sys.stdin.readline().rstrip()

for i in range(int(len(S)/2)):
    if not S[i] == S[-i-1]:
        print(0)
        exit(0)
print(1)