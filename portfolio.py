stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 200
}

print(" STOCK PORTFOLIO TRACKER ")

stock_name = input("Enter Stock Name: ").upper()

if stock_name in stock_prices:

    quantity = int(input("Enter Quantity: "))

    total = stock_prices[stock_name] * quantity

    print("\nStock Price:", stock_prices[stock_name])
    print("Total Investment Value =", total)

    file = open("portfolio.txt", "w")

    file.write("Stock Name: " + stock_name + "\n")
    file.write("Quantity: " + str(quantity) + "\n")
    file.write("Total Value: " + str(total))

    file.close()

    print("\nData saved in portfolio.txt")

else:
    print("Stock not found!")
