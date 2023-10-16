import re
a = input()
b = input()
match_ls = list(re.finditer(fr'(?={re.escape(b)})', a))

if match_ls:
    # Print the start and end positions of each match
    for match in match_ls:
        start = match.start()
        end = start + len(b) - 1
        print((start, end))
else:
    print((-1, -1))
