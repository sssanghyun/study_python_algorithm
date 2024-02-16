# 참고 https://hongcoding.tistory.com/33
import sys

X = int(sys.stdin.readline())

line = 0
end = 0

while X > end:
    line += 1
    end += line

diff = end - X
if line % 2 == 0:
    top = line - diff
    bottom = diff + 1
else:
    top = diff + 1
    bottom = line - diff

print(f"{top}/{bottom}")