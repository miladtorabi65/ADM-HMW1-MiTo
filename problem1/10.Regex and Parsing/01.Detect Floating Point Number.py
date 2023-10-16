import re
T = int(input())
for _ in range(T):
    inp = input()
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', inp)))
