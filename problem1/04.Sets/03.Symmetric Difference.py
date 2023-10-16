m = int(input())
input_data = input()
e_a = input_data.split()#Elements in a
a = set(map(int, e_a))
n = int(input(""))
input_data = input()
e_b = input_data.split() #Elements in b
b = set(map(int, e_b))
sorted1 = sorted(list(a.symmetric_difference(b)))
for i in sorted1:
    print(i)
