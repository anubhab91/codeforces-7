a = []
for i in range(input()):
  s = raw_input().split()
  if (not '3' in s and not '1' in s):
    a += [i + 1]
print str(len(a))
print ' '.join(map(str, a))
