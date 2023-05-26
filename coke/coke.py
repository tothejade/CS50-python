print("Amount Due: 50")
i = 0
while i < 50:
    x = int(input("Insert Coin: "))
    if x == 25 or x == 10 or x == 5:
        i += x
        if i >= 50:
            break
    else:
        i += 0
    print("Amount Due:", 50 - i)

print("Change Owed:", i - 50)