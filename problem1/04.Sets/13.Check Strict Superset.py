a = set(input().split()) #elements of set A
c=0
Z=0
n = int(input()) #The number of other sets
for i in range(n):
    input_data = set(input().split()) #elements of the other sets
    if a.issuperset(input_data):
        c += 1
    else:
        Z += 1
print('False' if Z != 0 else 'True')
