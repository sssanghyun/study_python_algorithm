import sys
from string import ascii_uppercase

alphabet = list(ascii_uppercase)

D = {}
n = 10

for a in alphabet:
    D[a] = n
    n += 1

S, B = sys.stdin.readline().rstrip().split()

result = 0
for i in range(-1, -len(S)-1, -1):
    if not S[i].isdigit():
        result += int(B) ** (-int(i)-1)*D[S[i]]
    else:
        result += int(B) ** (-int(i)-1)*int(S[i])

print(result)