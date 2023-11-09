import random


name_str=input("give me everybody name seperated by a comma.")
names=name_str.split(",")

# these are two ways that you can do this program
# num_items=len(names)
# random_choice= random.randint(0, num_items-1)

person_who_pay=random.choice(names)
print(f"{person_who_pay} should pay the bill")


