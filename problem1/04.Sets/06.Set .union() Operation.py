n = int(input())
a = set(map(int, input().strip().split(' ')))
m = int(input())
b = set(map(int, input().strip().split(' ')))
    
print(len(a.union(b)))
