import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

if a + b + c != 180:
    print("Error")
elif a == b == c:
    print("Equilateral")
elif a != b and a != c and b != c:
    print("Scalene")
else:
    print("Isosceles")