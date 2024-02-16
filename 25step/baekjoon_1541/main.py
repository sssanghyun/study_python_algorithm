import sys

c = sys.stdin.readline().rstrip().split('-')
result = 0

for i in range(len(c)):
    if '+' in c[i]:
        c[i] = sum(list(map(int, c[i].split('+'))))
    if i == 0:
        result = int(c[0])
    else:
        result -= int(c[i])
print(result)