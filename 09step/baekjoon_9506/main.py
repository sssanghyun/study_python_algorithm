import sys

while True:
    n = int(sys.stdin.readline())

    if n == -1:
        break
    result = []
    for i in range(1, n):
        if n % i == 0:
            result.append(i)

    if n == sum(result):
        print(f'{n} = {result[0]}', end="")
        for j in range(1, len(result)):
            print(f' + {result[j]}', end="")
        print()
    else:
        print(f'{n} is NOT perfect.')