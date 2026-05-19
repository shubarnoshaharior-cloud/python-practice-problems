status = input("Are you a member? ")

bill = float(input("Enter bill amount: "))

if status == "yes":
    final_bill = bill * 0.90
else:
    final_bill = bill

print("Final bill:", final_bill)