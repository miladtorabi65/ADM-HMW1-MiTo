import re
for _ in range(int(input())):
    u = input()
    if re.match(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})(?=[a-zA-Z0-9]{10}$)', u):
        print("Valid")
    else:
        print("Invalid")
