import re
for _ in range(int(input())):
    pat = r"(#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6})(?:[;,.)]{1})"
    res = re.findall(pat, input())
    for r in res:
        print(r)
