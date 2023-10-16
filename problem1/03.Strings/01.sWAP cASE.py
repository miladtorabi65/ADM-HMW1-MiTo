def swap_case(s):
    text=''
    for i in s:
            if i.isupper() == True:
                text += (i.lower())
            else:
                text += (i.upper())
    return text
