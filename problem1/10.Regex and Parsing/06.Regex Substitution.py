import re
n = int(input())
for _ in range(n):
    line = input()
    m = re.sub(r'(?<= )(&&|\|\|)(?= )', lambda match: "and" if match.group(0) == "&&" else "or", line)
    print(m)
