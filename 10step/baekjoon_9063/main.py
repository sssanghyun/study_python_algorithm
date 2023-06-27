import sys

x, y = [], []
input_data = []
result = 0
N = int(sys.stdin.readline())

for i in range(N):
    input_data = list(map(int, sys.stdin.readline().split()))
    x.append(input_data[0])
    y.append(input_data[1])

print((max(x) - min(x)) * (max(y) - min(y)))