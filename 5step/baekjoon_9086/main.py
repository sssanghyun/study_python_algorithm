import sys

T = int(sys.stdin.readline())

for _ in range(T):
    S = sys.stdin.readline().rstrip()
    print(f'{S[0]}{S[-1]}')