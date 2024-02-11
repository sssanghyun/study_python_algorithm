import sys

T = int(sys.stdin.readline())

for i in range(T):
    t = list(sys.stdin.readline().strip())
    s = []
    for j in t:
        if j == '(':
            s.append(t)
        else:
            if len(s) == 0:
                s.append('pop error')
                break
            else:
                s.pop()
    if len(s) == 0:
        print("YES")
    else:
        print("NO")