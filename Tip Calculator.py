
print("Welcome to Tip Calculator")
bill = float(input("what was the total bill? $"))
percentage_tip = int(input("what percentage tip would you like to give? 10,12 or 15?"))
people = int(input("how many people to split the bill?"))
percentage_cal = percentage_tip/100+1
total_bill = (bill/people) * percentage_cal
# using the format to have 2 decimal places:
final_bill = "{:.2f}".format(total_bill)
# total bill.
print(f"each person will pay: ${final_bill}")