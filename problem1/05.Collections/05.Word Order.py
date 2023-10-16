from collections import Counter
n = int(input())
l1 = []
for i in range(n):
    a = input()
    l1.append(a)
total = Counter(l1)
len_l = len(total)
print(len_l)
print(*total.values())
