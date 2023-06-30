# 참고 https://jinho-study.tistory.com/768
import sys

input_data = sorted(map(int, sys.stdin.readline().split()))
print(input_data[0] + input_data[1] + min(input_data[2], input_data[0] + input_data[1] -1))