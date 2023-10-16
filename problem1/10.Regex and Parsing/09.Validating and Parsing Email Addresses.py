import re
for _ in range(int(input())):
    a = input().split()
    name, email = a[0], a[1]
    if re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', email):
        print(name,email)
