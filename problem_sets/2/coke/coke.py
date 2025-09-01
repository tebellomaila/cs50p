def get_valid_coin(amount):
    """ Prompt the user for a coin until a valid denomination (25,10 or 5 cents) is inserted """
    while True:
        try:
            coin = int(input("Insert a coin: "))

            if coin in [25, 10, 5]:
                return coin
            else:
                # Ignore invalid coins and reprompt the user
                print(f"Amount Due: {amount}")
        except ValueError:
            # Handle non-integer input
            print(f"Amount Due: {amount}")

def main():
     cost = amount_due = 50
     amount_paid = 0

     # Initial prompt
     print(f"Amount Due: {cost}")

     while amount_paid < cost:
         coin = get_valid_coin(amount_due)
         amount_paid += coin
         amount_due = cost - amount_paid
         if amount_due > 0:
             print(f"Amount Due: {amount_due}")

     change_owed = amount_paid - cost
     print(f"Change Owed: {change_owed}")


if __name__ == "__main__":
    main()
