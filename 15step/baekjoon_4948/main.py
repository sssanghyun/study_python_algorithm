import sys
import math

def is_prime_num(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return 0
    return 1

arr = [is_prime_num(i) for i in range(0, (123456)*2+1)]

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    count = 0
    for j in range(n+1, 2*n+1):
        if arr[j] == 1:
            count += 1
    print(count)