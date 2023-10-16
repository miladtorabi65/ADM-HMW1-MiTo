from collections import Counter
x = int(input()) # the number of shoes
s = input().split() #list of all the shoe sizes in the shop
s_ls = list(map(int, s)) 
n = int(input()) #the number of customers.
sum1 = 0
available = Counter(s_ls)
for i in range(n):
    xx = input().split() #the shoe size desired by the customer and xi , the price of the shoe.
    price = int(xx[1])
    size = int(xx[0])
    if available[size] > 0:
        sum1 += price
        available[size] -= 1    
print(sum1)
