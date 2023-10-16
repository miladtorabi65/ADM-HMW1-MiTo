from collections import defaultdict
inp = input().split()
n = int(inp[0]) #the words belonging to group A
m = int(inp[1]) #he words belonging to group B
d = defaultdict(list)
for i in range(1, n + 1):
    s = input()
    d[s].append(str(i))
for i in range(m):
    a = input()
    r = d.get(a, ['-1'])
    print(' '.join(r) if r != ['-1'] else -1)
