if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t1=tuple(integer_list)
    print(hash(t1))
