# 참고 https://ywtechit.tistory.com/194
import sys

N = int(sys.stdin.readline())
stack = []
s = list(map(int, sys.stdin.readline().split()))

# 차례
line = 1

while s:
    if s[0] == line:
        s.pop(0)
        line += 1
    else:
        stack.append(s.pop(0))

    while stack:
        if stack[-1] == line:
            stack.pop()
            line += 1
        else:
            break

if len(stack) == 0:
    print('Nice')
else:
    print('Sad')