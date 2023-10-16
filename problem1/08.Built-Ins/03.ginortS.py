a = input()
# using the lamnda function to filter and then sort
a = sorted(a,key = lambda x:(x.isdigit() and int(x)%2==0, x.isdigit(),x.isupper(),x.islower(),x))
print(*(a),sep = '')
