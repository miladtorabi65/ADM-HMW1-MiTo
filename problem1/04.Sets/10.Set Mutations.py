n = int(input()) #the number of elements in set A
l = set(map(int, input().split())) #list of elements in set A
n_stes = int(input()) #he number of other sets
for _ in range(n_stes):
    cmd, *args = input().split()
    get_set = set(map(int, input().split()))
    if cmd == 'intersection_update':
        l.intersection_update(get_set)
    elif cmd == 'difference_update':
        l.difference_update(get_set)
    elif cmd == 'symmetric_difference_update':
        l.symmetric_difference_update(get_set)
    elif cmd == 'update':
        l.update(get_set)
print(sum(l))
