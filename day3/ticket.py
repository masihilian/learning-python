print("welcom to the rollercoaster")
bill= 0
height=int(input("what is your height? "))
age=int(input("what is your age ? "))
if height>=120:
    if age>=45 and age<=55:
        print("you have free ticket")
    elif age>=18:
        bill=12
        print(f"adult pay {bill}$")
    elif age>=12:
        bill=7
        print(f"youth pay {bill}$")
    else:
        bill=5
        print(f"child pay {bill}$")
    extra_money = input("do you want photo? y or n ")
    if extra_money == "y":
        bill+=3
    print(f"your final bill is {bill}")

else:
    print("your not tall enought ")