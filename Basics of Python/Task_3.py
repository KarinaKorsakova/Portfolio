coffee_price = 5
cake_price = 3
my_money = int(input("Input your cash (UAH): "))
if coffee_price <= my_money < coffee_price + cake_price:
    print("Good day with coffee")
elif my_money >= coffee_price + cake_price:
    print("Good day with coffee and cake")
else: 
    print("Bad day")