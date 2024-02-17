# 참고 https://night-knight.tistory.com/entry/%EB%B0%B1%EC%A4%801654-%EB%9E%9C%EC%84%A0-%EC%9E%90%EB%A5%B4%EA%B8%B0-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys

K, N = map(int, sys.stdin.readline().split(' '))
lan = [int(sys.stdin.readline()) for _ in range(K)]
s, e = 1, max(lan)

while s <= e:
    mid = (s + e) // 2
    count = 0
    for i in lan:
        count += i // mid

    if count >= N:
        s = mid + 1
    else:
        e = mid - 1

print(e)