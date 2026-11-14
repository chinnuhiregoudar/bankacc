# Bank Account Management System

name = input("Enter customer name: ")
balance = float(input("Enter initial account balance: "))

deposit = float(input("Enter amount to deposit: "))
balance = balance + deposit

print("Balance after deposit:", balance)

withdraw = float(input("Enter amount to withdraw: "))

if withdraw > balance:
    print("Insufficient balance")

elif balance - withdraw < 1000:
    print("Minimum balance of 1000 must be maintained")

else:
    balance = balance - withdraw
    print("Withdrawal successful")

print("\nCustomer Name:", name)
print("Updated Account Balance:", balance)