# Estimate yearly Interest




print("How many years will you be saving?")
years = int(input("Enter years: "))

print(" ")

print("How much money is currently in your account?")
principal = float(input("Enter current amount in account: "))

print(" ")

print("How much money do you plan on investing monthly?")
monthly_invest = float(input("Enter amount: "))

print(" ")

print("What do you estimate will be the yearly interest of this investment?")
interest = float(input("Enter the percentage amount: "))

print(" ")
print(" ")

monthly_invest = monthly_invest * 12
final_amount = 0
interest = interest / 100


for i in range(0, years):
    if final_amount == 0:
        final_amount = principal
        
    final_amount = (final_amount + monthly_invest) * (1 + interest)
    
print("This is how much you would have in your account after {} years: ".format(years) + str(final_amount))

