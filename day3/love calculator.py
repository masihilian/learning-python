print("welcome to love calculator")
name1=input("what is your name ? \n")
name2=input("what is thier name? \n")
combined_string=name1+name2
lower_name=combined_string.lower()

t=lower_name.count("t")
r=lower_name.count("r")
u=lower_name.count("u")
e=lower_name.count("e")
l=lower_name.count("l")
o=lower_name.count("o")
v=lower_name.count("v")
e=lower_name.count("e")
true=t+r+u+e
love=l+o+v+e
total=int(str(true)+str(love))

if total<10 or total>90:
    print(f"your socre is  {total}%, you go together like coke and mentos ")
elif total>=40 and total<=50:
    print(f"your score is  {total}%, you are alright together ")
else :
    print(f"your score is  {total}% ")