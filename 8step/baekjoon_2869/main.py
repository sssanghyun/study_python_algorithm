import sys, math

A, B, V = map(int, sys.stdin.readline().split())

days = 0

diff = A - B
V -= A
days = math.ceil(V / diff)
print(days+1)
