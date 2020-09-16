while True:
    try:
        change = float(input("Change owed: "))
        if 0 < change:
            break
    except ValueError:
        True

change = int(change*100)
quarters = int(change / 25)
remain1 = change % 25
dimes = int(remain1 / 10)
remain2 = remain1 % 10
nickels = int(remain2 / 5)
pennies = int(remain2 % 5)
coins = (quarters + dimes + nickels + pennies)
print(coins)