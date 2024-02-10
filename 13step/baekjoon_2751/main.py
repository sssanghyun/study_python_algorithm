#https://kill-xxx.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-10989%EB%B2%88-%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-3-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EC%B4%88%EA%B3%BC-%EC%98%A4%EB%A5%98-%ED%95%B4%EA%B2%B0 참고
import sys

N = int(sys.stdin.readline())

arr = [0] * 10001

for _ in range(N):
    arr[int(sys.stdin.readline())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)