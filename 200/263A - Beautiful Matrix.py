for i in range(5):
  x = map(int, raw_input().split())
  if 1 in x:
    print abs(x.index(1) - 2) + abs(i - 2)
    break
