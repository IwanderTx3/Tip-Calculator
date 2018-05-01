total_amount = float(input("Please enter the amount of your bill: "))
tip_percent = float(input("Please enter the percentage you want to tip: "))
final_bill = round(( total_amount * ( tip_percent / 100) + total_amount), 2)
print (f"total amount to pay: ${ final_bill } ")
