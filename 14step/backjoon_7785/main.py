import sys

N = int(sys.stdin.readline())
people = set()

for _ in range(N):
    name, work = sys.stdin.readline().split()
    if work == 'enter':
        people.add(name)
    else:
        people.remove(name)

people = list(people)
people.sort(reverse=True)
for name in people:
    print(name)