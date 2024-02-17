# https://ooyoung.tistory.com/74
# 참고
import sys

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
S = sys.stdin.readline().rstrip()

for i in croatia:
    S = S.replace(i, '1')
print(len(S))