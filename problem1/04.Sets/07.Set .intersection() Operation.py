n = int(input()) # the number of students who have subscribed to the English newspaper.
r = set(map(int, input().strip().split(' '))) #roll numbers of English students
m = int(input()) #he number of students who have subscribed to the French newspaper.
b = set(map(int, input().strip().split(' ')))   #roll numbers of French students. 
print(len(r.intersection(b)))
