import sys

index = 1
six_count = 1
result = 0
N = int(sys.stdin.readline())
N -= 1

while N > 0:
    N = N - 6 * six_count
    result += 1
    six_count += 1

result += 1
print(result)