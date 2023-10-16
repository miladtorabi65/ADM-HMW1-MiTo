def wrap(string, max_width):
    start=0
    newstring=''
    for i in range(int(len(string)/max_width)+1):
        r=string[start:max_width+start]+'\n'
        newstring = newstring+r
        start=start+max_width
    return newstring
  if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
