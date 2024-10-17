print("Your coffe costs 75p. This machine accepts only 50p, 20p, 10p and 5p coins.")
coin_inserted = 0
price = int(75)
while int(coin_inserted) < 75:
    coin_inserted = int(input("Enter the inserted coin value: "))
    if coin_inserted == 5:
        price = price - coin_inserted
        print("You still have to pay "+str(price))
    elif coin_inserted == 10:
        price = price - coin_inserted
        print("You still have to pay "+str(price))
    elif coin_inserted == 20:
        price = price - coin_inserted
        print("You still have to pay "+str(price))
    elif coin_inserted == 50:
        price = price - coin_inserted
        print("You still have to pay "+str(price))
    else:
        print("The coin value is incorrect")
    if price <= 0:
        print("You've successfully purchased the coffee.")
        break