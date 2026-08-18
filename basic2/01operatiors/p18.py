amt = 10000

while True:

    n = input(
        "PLEASE SELECT AN OPTION\n"
        "1. BALANCE CHECK\n"
        "2. WITHDRAW\n"
        "3. DEPOSIT\n"
        "4. EXIT\n"
        ":- "
    )

    match n:

        case '1':
            print(f"\nCURRENT ACCOUNT BALANCE: ₹{amt}")
            print("==========================================")

        case '2':
            a = int(input("ENTER WITHDRAWAL AMOUNT: ₹"))

            if a < amt:
                amt -= a
                print(f"\nTRANSACTION SUCCESSFUL")
                print(f"₹{a} HAS BEEN WITHDRAWN FROM YOUR ACCOUNT.")
                print(f"REMAINING BALANCE: ₹{amt}")
                print("==========================================")
            else:
                print("\nTRANSACTION FAILED")
                print("INSUFFICIENT ACCOUNT BALANCE.")
                print("==========================================")

        case '3':
            b = int(input("ENTER DEPOSIT AMOUNT: ₹"))

            amt += b
            print(f"\nDEPOSIT SUCCESSFUL")
            print(f"₹{b} HAS BEEN DEPOSITED INTO YOUR ACCOUNT.")
            print(f"UPDATED BALANCE: ₹{amt}")
            print("==========================================")

        case '4':
            print("\nTRANSACTION TERMINATED.")
            print("THANK YOU FOR USING OUR ATM.")
            print("HAVE A GREAT DAY!")
            exit()

        case _:
            print("\nINVALID OPTION")
            print("PLEASE SELECT A VALID OPTION FROM 1 TO 4.")
            print("==========================================")