import sys

N, M = map(int, sys.stdin.readline().split())
input_data = list(map(int, sys.stdin.readline().split()))
max = 0

for i in range(N-2):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if input_data[i] + input_data[j] + input_data[k] == M:
                print(M)
                exit(0)
            elif input_data[i] + input_data[j] + input_data[k] < M:
                if input_data[i] + input_data[j] + input_data[k] > max:
                    max = input_data[i] + input_data[j] + input_data[k]
print(max)