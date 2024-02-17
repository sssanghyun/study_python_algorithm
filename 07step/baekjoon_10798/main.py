import sys

L = []
max = 0
for n in range(5):
    L.append(list(sys.stdin.readline().rstrip()))
    if len(L[n]) > max:
        max = len(L[n])

for i in range(max):
    for j in range(5):
        try:
            print(L[j][i], end='')
        except:
            pass