k = int(input()) #, the size of each group
room_n = input().split() #unordered elements of the room number list
# convert it to int list
for i in range(len(room_n)):
    room_n[i] = int(room_n[i])
x = (sum(set(room_n)) * k - sum(room_n))    
captainroom = x // (k - 1)
print(captainroom)
