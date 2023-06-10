import sys

# N = int(sys.stdin.readline())
# for i in range(N):
#     star = ""
#     for _ in range(i + 1):
#         star += "*"
#     print(f'{star:>5}')

# 출력 형식이 잘못 되어 재작성
# https://claude-u.tistory.com/20 참고
N = int(sys.stdin.readline())
for i in range(1, N+1):
    print(" " * (N - i) + "*" * i)