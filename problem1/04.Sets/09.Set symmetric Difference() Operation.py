n = int(input()) #number of students who have subscribed to the English newspaper.
r = set(map(int, input().strip().split(' '))) #English newspaper.
m = int(input()) #number of students who have subscribed to the French newspaper.
b = set(map(int, input().strip().split(' '))) #French newspaper.
print(len(r.symmetric_difference(b)))
