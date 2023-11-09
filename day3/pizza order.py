print("welcome to my fastfood")
size=input("what size you want ? S,M or L ")
add_pepperoni = input("do you want pepperoni? Y or N ")
exra_cheese= input("do you wnat extra exra cheese ? Y or N  ")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
if add_pepperoni=="Y":
    if size =="S":
        bill+=2
    else:
        bill+=3
if exra_cheese=="Y":
    bill+=1
print(f"your final bill is {bill}")