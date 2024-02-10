import sys

N = list(str(sys.stdin.readline().split()[0]))

N.sort(reverse=True)

print(''.join(N))