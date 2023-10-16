if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=list(arr)
    l.sort()
    max_l=max(l)
    print(l[(l.index(max_l))-1])
