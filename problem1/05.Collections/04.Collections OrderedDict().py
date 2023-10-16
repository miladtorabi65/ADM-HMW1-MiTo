from collections import OrderedDict
items_dict = OrderedDict()
n = int(input()) # the number of items N
for _ in range(n): 
    name_price = input().rsplit(' ', 1) #the item's name and price
    item = name_price[0]
    price = int(name_price[1])
    items_dict[item] = items_dict.get(item, 0) + price
for item, total_price in items_dict.items():
    print(item, total_price)
