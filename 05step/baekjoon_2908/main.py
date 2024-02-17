import sys

a = list(sys.stdin.readline().rstrip())
a[0], a[2] = a[2], a[0]
a[4], a[-1] = a[-1], a[4]

a = "".join(a)
a = a.split()
print(max(a))
