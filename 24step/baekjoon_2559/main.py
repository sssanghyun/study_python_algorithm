import sys

N, K = map(int, sys.stdin.readline().split(' '))
temp = list(map(int, sys.stdin.readline().split(' ')))
s = [0 for _ in range(N)]

# 누적합
s[0] = temp[0]
for i in range(1, N):
    s[i] = temp[i] + s[i - 1]

i = 0
# 누적합으로 구간합
s_k = [0 for _ in range(N-K+1)]
while True:
    j = i + K - 1
    if j >= N:
        break
    if i == 0:
        s_k[i] = s[j]
    else:
        s_k[i] = s[j] - s[i - 1]
    i += 1

print(max(s_k))