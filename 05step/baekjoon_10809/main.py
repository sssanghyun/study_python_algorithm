import sys
from string import ascii_lowercase

S = sys.stdin.readline().rstrip()
al = list(ascii_lowercase)

for s in al:
    print(S.find(s), end=" ")