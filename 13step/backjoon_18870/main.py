# 참고 https://gudwns1243.tistory.com/52
import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

cheack_arr = sorted(list(set(arr)))

dic = {cheack_arr[i] : i for i in range(len(cheack_arr))}

for i in arr:
    print(dic[i], end=' ')