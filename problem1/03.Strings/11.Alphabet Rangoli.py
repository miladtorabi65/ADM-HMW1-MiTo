def print_rangoli(n):

    alpha = 'abcdefghijklmnopqrstuvwxyz'
    l = list()

    for i in range(n):
        substring = "-".join(alpha[i:n])
        pattern_line = substring[::-1] + substring[1:]
        l.append(pattern_line)

    max_width = len(l[0])

    for i in range(n - 1, 0, -1):
        print(l[i].center(max_width, '-'))
        
    for i in range(n):
        print(l[i].center(max_width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
