from collections import deque
t_num = int(input()) #the number of test cases.
for i in range(t_num):
    n_cubes = input() #the number of cubes.
    sideLengths1 = input().split() #the sideLengths of each cube in that order.
    sideLengths = deque(map(int, sideLengths1))
    flag = 1
    l = len(sideLengths)
    for j in range(l- 1):
        if sideLengths[0] >= sideLengths[1]:
            sideLengths.popleft()
        elif sideLengths[-1] >= sideLengths[-2]:
            sideLengths.pop()
        else:
            flag = 0
            break
    if flag ==1:
        print("Yes")
    else:
        print("No")
