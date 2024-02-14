import sys

def recursion(s, l, r, c):
    c += 1
    if l >= r: return 1, c
    elif s[l] != s[r]: return 0, c
    else: return recursion(s, l+1, r-1, c)

def isPalindrome(s, c):
    return recursion(s, 0, len(s)-1, c)

T = int(sys.stdin.readline())

for _ in range(T):
    s = sys.stdin.readline().rstrip()
    c = 0
    result = isPalindrome(s, c)
    print(result[0], result[1])