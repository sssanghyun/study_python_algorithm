import sys

N = int(sys.stdin.readline())
card_N = set(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline())
card_M = list(map(int, sys.stdin.readline().strip().split()))

for card in card_M:
    if card in card_N:
        print(1, end=' ')
    else:
        print(0, end=' ')