import sys

N = int(sys.stdin.readline())

i = 666
while True:
    if str(i).find('666') > -1:
        N = N-1
    if N == 0:
        print(i)
        break
    i = i + 1