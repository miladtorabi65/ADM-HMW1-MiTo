n = int(input()) #students who have subscribed to the English newspaper.
r = set(map(int, input().strip().split(' '))) #list of student roll numbers who have subscribed to the English newspaper.
m = int(input()) #the number of students who have subscribed to the French newspaper.
b = set(map(int, input().strip().split(' '))) #list of student roll numbers who have subscribed to the French newspaper.
print(len(r.difference(b)))
