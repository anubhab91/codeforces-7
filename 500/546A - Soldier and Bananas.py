l = map(int, raw_input().split(' '))
print max(l[0] * (l[2] + l[2] * l[2]) / 2 - l[1], 0)
