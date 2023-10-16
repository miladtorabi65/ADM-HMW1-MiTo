import re
for _ in range(int(input())):
    n = input()
    a = '^[789][0-9]{9}$'
    print("YES" if bool(re.match(a, n)) else "NO")
