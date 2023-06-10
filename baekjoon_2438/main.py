import sys

N = int(sys.stdin.readline())
for i in range(N):
    star = ""
    for _ in range(i+1):
        star += "*"
    print(star)