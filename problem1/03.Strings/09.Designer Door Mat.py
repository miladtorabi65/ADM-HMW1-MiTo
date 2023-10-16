n = input()
linput = n.split()
n, m = int(linput[0]), int(linput[1])
#the upper part of the center line
for i in range(int(n/2)):
    patern=i+i+1   #the number of .|. in each row
    no_patern=m-(patern*3)  #the number of - in each side of the ".|." shape in a row
    print(("-"*int(no_patern/2))+(".|."*patern)+"-"*int(no_patern/2))
#the center line
print(("-"*int((m-7)/2))+"WELCOME"+("-"*int((m-7)/2)))
#the lower part of the center line
for i in range(int(n/2)):
    no_patern = 6 + (i * 6)  # the number of - in each side of the ".|." shape in a row
    patern=int((m-(no_patern))/3)   #the number of .|. in each row
    print(("-"*int(no_patern/2))+(".|."*patern)+"-"*int(no_patern/2))
