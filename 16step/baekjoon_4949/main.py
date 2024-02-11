import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == '.':
        break

    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack[-1] != '(':
                stack.append("pop err")
                break
            else:
                stack.pop()
        elif i == '[':
            stack.append(i)
        elif i == ']':
            if len(stack) == 0 or stack[-1] != '[':
                stack.append("pop err")
                break
            else:
                stack.pop()
    if len(stack) == 0:
        print("yes")
    else:
        print("no")