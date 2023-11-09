import random

choice= int(input("what do you want ? rock 0, papaer 1,scissors 2 .\n"))

rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


if choice==0:
    print (rock)
    print ("\n computer chose\n")
    random_chose= random.randint(0, 2)
    if random_chose==0:
        print(f"{rock} \n nothing happen here")
    elif random_chose==1:
        print(f"{paper} \n you lose the game ")
    else:
        print(f"{scissors} \n you win the game ")
elif choice==1:
        print (paper)
        print ("\n computer chose\n")
        random_chose= random.randint(0, 2)
        if random_chose==0:
            print(f"{rock} \n you win the game")
        elif random_chose==1:
            print(f"{paper} \n nothing happen here ")
        else:
            print(f"{scissors} \n you lose the game")
elif choice==2:
        print (scissors)
        print ("\n computer chose\n")
        random_chose= random.randint(0, 2)
        if random_chose==0:
            print(f"{rock} \n you lose the game")
        elif random_chose==1:
            print(f"{paper} \n you win the game ")
        else:
            print(f"{scissors} \n nothing happen here ")
else:
     print("you enter wrong number !!!!!!!")
