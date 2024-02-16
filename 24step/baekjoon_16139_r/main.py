# 참고 https://velog.io/@slbin-park/%EB%B0%B1%EC%A4%80-16139%EB%B2%88-%EC%9D%B8%EA%B0%84-%EC%BB%B4%ED%93%A8%ED%84%B0-%EC%83%81%ED%98%B8%EC%9E%91%EC%9A%A9-%ED%8C%8C%EC%9D%B4%EC%8D%AC
import sys

S = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())

# 알파벳 전체 갯수 만큼
dp = [[0 for i in range(len(S))] for i in range(26)]

for i in range(26):
    for j in range(len(S)):
        if chr(i + 97) == S[j]:
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j - 1] + 1
        else:
            dp[i][j] = dp[i][j - 1]

for _ in range(N):
    s, i, j = sys.stdin.readline().rstrip().split(' ')
    i = int(i)
    j = int(j)
    if i == 0:
        print(dp[ord(s) - 97][j])
    else:
        print(dp[ord(s) - 97][j] - dp[ord(s) - 97][i - 1])
