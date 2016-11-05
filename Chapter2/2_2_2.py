price = 24.95
discount = 0.4
first_shipping_cost = 3
additional_shipping_cost = 0.75
count = 60

book_price = price * count * (1 - discount)
shipping_cost = first_shipping_cost + additional_shipping_cost * (count-1)  
total = book_price + shipping_cost

print(total) 
