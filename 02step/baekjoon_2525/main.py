hour, min = map(int, input().split())
time = int(input())
min += time
if min >= 60:
    hour += min // 60
    if hour >= 24:
        hour -= 24
    min -= min // 60 * 60
print(f"{hour} {min}")