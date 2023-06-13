import sys

N = int(sys.stdin.readline())
count = 0

for _ in range(N):
    S = sys.stdin.readline().rstrip()
    result = ""
    index = 0
    for i in S:
        index += 1
        if result != "" and result[-1] == i:
            if index == len(S):
                count += 1
            pass
        else:
            if result.find(i) > -1:
                break
            else:
                result += i
                if index == len(S):
                    count += 1
print(count)