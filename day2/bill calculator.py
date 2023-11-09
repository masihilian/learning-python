print("welcom to the tip calculator \n ")
bill = float(input("what was the toatal bill?"))
tip = int(input("how much tip would you give ? 10 12 or 15? "))
people = int(input("how mane peolpe you want to splite the bill?"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip/people
final_amount=round(bill_per_person, 2)
final_amount= "{:.2f}".format(bill_per_person)
print(f"each person should pay   {final_amount}")

