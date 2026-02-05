ROWS = 3
COLS = 5

all_seats = [
    [f"{chr(65 + r)}{c}" for c in range(COLS)]
    for r in range(ROWS)
]

reserved = {}

def seats():
    for i in range(ROWS):
        print(f"ROW {i+1}:\t", end='')
        for j in range(COLS):
            seat = all_seats[i][j]
            print("X" if seat in reserved else seat, end=' ')
        print()

seats()

# print(all_seats)
# print(any("A1" in row for row in all_seats))
# print(any("A01" in row for row in all_seats))

# Discount: Less than 5,000 (No), 5,000 to 20,000 (5%), More than 20,000 (10%)

# orders = {}
# state = True

# def menu():
#     print("\nOptions:\n")
#     print("1. Proceed with the same customer.")
#     print("2. Proceed with a different customer.")
#     print("3. Display total bill per customer.")
#     print("4. Exit.\n")

# def get_input(what):
#     if what == "customer":
#         return input("Enter customer ID: ")
#     elif what == "amount":
#         return float(input("Enter amount: "))
#     return None

# def set_order(cid, amt):
#     if cid in orders:
#         orders[cid] += amt
#     else:
#         orders[cid] = amt

# def display_total():
#     print("\nCUSTOMER BILL SUMMARY\n")
#     print("ID\tAMOUNT\t\tDISCOUNT\tPAYABLE")
#     for cid, total in orders.items():
#         # print(f"{cid} → {total}")
#         discount = 0
#         if total > 20000:
#             discount = total * 0.1
#         elif total > 5000:
#             discount = total * 0.05
#         print(f"{cid}\t{total}\t\t{discount}\t\t{total-discount}")

# menu()

# customer = None

# while state:
#     match int(input("Enter your choice: ")):
#         case 1:
#             if customer is None:
#                 customer = get_input("customer")
#             amount = get_input("amount")
#             set_order(customer, amount)

#         case 2:
#             customer = get_input("customer")
#             amount = get_input("amount")
#             set_order(customer, amount)

#         case 3:
#             display_total() 

#         case _:
#             display_total()
#             state = False

# print("Program terminated.")

# # MAX_ATTEMPTS = 3

# # credentials = {
# #     'admin': 'admin',
# #     'user': 'password',
# # }

# # attempts = {}

# # state = True

# # print("\n"+"*" * 19)
# # print("*"*3+"    LOGIN\t"+"*"*3)
# # print("*" * 19 +"\n")
    

# # while state:
# #     print("Enter EXIT to exit\n")
# #     username = input("Username: ")
    
# #     if username.lower() == "exit":
# #         print("Program Terminated")
# #         state = False
# #         break
    
# #     if credentials.get(username) is not None:    
        
# #         attempts.setdefault(username, 0)
        
# #         if attempts.get(username) >= MAX_ATTEMPTS:
# #             print(f"\nNo more login attempts for username: {username}\n")
# #             continue
        
# #         password = input("Password: ")
        
# #         if credentials.get(username) == password:
# #             print("Logged In\n")
# #             state = False
            
# #         else:
# #             count = attempts[username] + 1
# #             attempts.update({username: count})
# #             print(f"\nInvalid password, try logging in again! Remaining attempts: {MAX_ATTEMPTS - count}\n")
        
# #     else:
# #         print("\n*** USERNAME NOT FOUND ***\n")

# # customer = None
# # print(customer)

# # Discount: Less than 5,000 (No), 5,000 to 20,000 (5%), More than 20,000 (10%)

