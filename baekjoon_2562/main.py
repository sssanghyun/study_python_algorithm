import sys

l = list()
for _ in range(9):
    l.append(int(sys.stdin.readline()))

print(max(l))
print(l.index(max(l))+1)