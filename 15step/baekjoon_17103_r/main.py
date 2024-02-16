# 참고 https://portable-paper.tistory.com/entry/17103-%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90-%ED%8C%8C%ED%8B%B0%EC%85%98-python
import sys

n = 1000000
a = [False,False] + [True] * (n - 1)
primes = []

for i in range(2, n + 1):
  if a[i]:
    primes.append(i)
    for j in range(2 * i, n + 1, i):
        a[j] = False

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    count = 0

    for i in range(2, N//2+1):
        if a[i] and a[N-i]:
            count += 1
    print(count)