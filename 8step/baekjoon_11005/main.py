import sys
from string import ascii_uppercase

alphabet = list(ascii_uppercase)

D = {}
n = 10

for a in alphabet:
    D[n] = a
    n += 1

S, B = map(int, sys.stdin.readline().rstrip().split())

result = []

while True:
    temp = S % B
    S = S // B
    if temp >= 10:
        result.insert(0, D[temp])
    else:
        result.insert(0, str(temp))
    if S == 0:
        break
print(''.join(result))