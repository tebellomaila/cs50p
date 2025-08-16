def insert_coin(amount):
    while True:
        coin = int(input(f"Insert Coin: "))

        if coin in [25, 10, 5]:
            return coin

        print(f"Amount Due: {amount}")


def calculate_change(amount_due, cost):
    return amount_due - cost


def main():
     amount_due = 0

     cost = 50

     print(f"Amount Due: {cost}")

     while amount_due < cost:
         coin = insert_coin(cost - amount_due)

         amount_due += coin

         if amount_due < cost:
             print(f"Amount Due: {cost - amount_due}")

     change_owed = calculate_change(amount_due, cost)
    
     print(f"Change Owed: {change_owed}")



if __name__ == "__main__":
    main()
