# 참고 https://claude-u.tistory.com/446
import sys

N, M = map(int, sys.stdin.readline().split(' '))
tree = list(map(int, sys.stdin.readline().split(' ')))
s, e = 1, max(tree)

while s <= e:
    mid = (s + e) // 2
    count = 0
    for i in tree:
        if i > mid:
            count += i - mid
    if count >= M:
        s = mid + 1
    else:
        e = mid - 1

print(e)