def count_substring(string, sub_string):
    c=0
    for i in string:
        if string.find(sub_string)!=-1:
            c+=1
            string=string[string.find(sub_string)+1:]
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
