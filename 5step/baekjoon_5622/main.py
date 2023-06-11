import sys

S = sys.stdin.readline().rstrip()

time = 0

for s in S:
    if s in ['A', 'B', 'C']:
        time += 3
    elif s in ['D', 'E', 'F']:
        time += 4
    elif s in ['G', 'H', 'I']:
        time += 5
    elif s in ['J', 'K', 'L']:
        time += 6
    elif s in ['M', 'N', 'O']:
        time += 7
    elif s in ['P', 'Q', 'R', 'S']:
        time += 8
    elif s in ['T', 'U', 'V']:
        time += 9
    elif s in ['W', 'X', 'Y', 'Z']:
        time += 10

print(time)