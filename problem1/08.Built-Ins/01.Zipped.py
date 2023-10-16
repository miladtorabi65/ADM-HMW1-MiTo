a = input()
a = a.split()
n, x = int(a[0]), int(a[1])
scores = []
for i in range(x):
    scores.append(list(map(float, input().split())))
for i in zip(*scores):
    print(sum(i) / len(i))
