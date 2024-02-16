# 참고 https://velog.io/@qtly_u/DP-%EB%B0%B1%EC%A4%80-1463%EB%B2%88-1%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0
# n일 때 몇번 연산횟수가 몇회인지 저장해두고 사용
import sys

X = int(sys.stdin.readline())
dp = [0] * 1_000_001

for i in range(2, X+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
print(dp[X])