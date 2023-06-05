a, b, c = map(int, input().split())
result = 0
if a == b == c:
    result = a * 1000 + 10000
elif a == b or b == c:
    result = b * 100 + 1000
elif a == c:
    result = a * 100 + 1000
else:
    result = max(a, b, c) * 100
print(result)