# 참고 https://kevinitcoding.tistory.com/entry/%EB%B0%B1%EC%A4%80Python-24313%EB%B2%88-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%88%98%EC%97%85-%EC%A0%90%EA%B7%BC%EC%A0%81-%ED%91%9C%EA%B8%B0-1-%EB%AC%B8%EC%A0%9C
import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

fn = a1 * n0 + a0
gn = c * n0

if fn <= gn and a1 <= c:
    print(1)
else:
    print(0)