def merge_the_tools(string, k):
    # 
    t = []
    len_t = 0
    for item in string:
        len_t += 1
        if item not in t:
            t.append(item)
        if len_t == k:
            print (''.join(t))
            t = list()
            len_t = 0
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
