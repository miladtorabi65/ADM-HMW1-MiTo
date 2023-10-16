n = int(input()) #the number of test cases T
for i in range(n):
    n_a = int(input()) #the number of elements in set A
    set_a = set(map(int, input().split())) #elements of set A
    n_b = int(input()) #the number of elements in set B
    set_b = set(map(int, input().split())) #elements of set B
    print("True" if len(set_a - set_b) == 0 else "False")
