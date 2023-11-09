height = input("enter your height in m : ")
weight = input("enter your weight in kg : ")
bmi = round(weight/height **2)
if bmi<=18.5:
    print(f"you bmi is {bmi} and you have underweight")
elif bmi<=25:
    print(f"you bmi is {bmi} and you have normal weight")
elif bmi<=30:
    print(f"you bmi is {bmi} and you have overwight")
elif bmi<=35:
    print(f"you bmi is {bmi} and you have obese")
else:
    print(f"you bmi is {bmi} and you have over obese")