# Calculate the total value of items based on stock and price

# Menu items
menu_list = ["coffee" ,"sandwich" , "tea" , "smoothie"]

# stock value of each item
stock = {"coffee" : 70 , 
             "sandwich" : 40 , 
             "tea" : 60, 
             "smoothie" : 80
             }

# price of each item 
price = {"coffee" : 2.25 , 
             "sandwich" : 3.35 , 
             "tea" : 2.0, 
             "smoothie" : 2.50
             }


# calculate the total stock worth in the cafe
total_stock = sum(stock[item] * price[item] for item in menu_list)

# print the result of the calculation
print(total_stock)


