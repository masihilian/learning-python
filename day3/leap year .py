year = int(input("what year do you want to find leep?"))

if year % 4 ==0:
    if year % 100 ==0:
     if year%400==0:
      print('leap')
     else:
      print('not leap')
    else:
      print("leap")
else:
    print("not leap")
