import sys

n = int(sys.stdin.readline())
f = [0] * (n+1)
f[1] = 1
f[2] = 1

count_fib = 0
count_fibonacci = 0

def fib(n):
    global count_fib
    if n == 1 or n == 2:
        return 1
    else:
        count_fib += 1
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    global count_fibonacci
    for i in range(3, n+1):
        count_fibonacci += 1
        f[i] = f[i-1] + f[i-2]
    return count_fibonacci

fib(n)
print(count_fib+1)
print(fibonacci(n))