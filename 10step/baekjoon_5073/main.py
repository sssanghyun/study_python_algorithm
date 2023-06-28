import sys

while True:
    input_data = list(map(int, sys.stdin.readline().split()))
    input_data.sort()
    if input_data[0] == 0 and input_data[1] == 0 and input_data[2] == 0:
        break
    elif input_data[2] >= input_data[0] + input_data[1]:
        print("Invalid")
    elif input_data[0] == input_data[1] == input_data[2]:
        print("Equilateral")
    elif input_data[0] != input_data[1] != input_data[2]:
        print("Scalene")
    else:
        print("Isosceles")