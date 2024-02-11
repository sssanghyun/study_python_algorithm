import sys

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

result_p = int(B * D)
result_c = int(A * D + C * B)

AA, BB = result_c, result_p
while BB:
    AA, BB = BB, AA % BB
print(int(result_c / AA), int(result_p / AA))