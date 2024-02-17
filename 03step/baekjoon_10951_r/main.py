import sys

# 런타임에러 참고 https://codingpractices.tistory.com/entry/%EB%B0%B1%EC%A4%80-10951%EB%B2%88-AB-4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break