year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    print("leap")
elif year % 100 == 0:
    print("not leap")
elif year % 400 == 0: 
            print("leap")
else:
    print("not leap")