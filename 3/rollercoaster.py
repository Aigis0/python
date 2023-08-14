bill = 0
height = int(input("what is your height: "))
age = int(input("what is your age: "))
if height >= 120:
    print("You Can ride the rollercoaster")
    if age < 12:
        bill += 5
        print(f"Children tickets are : ${bill}")
    elif age <= 18:
        bill += 7
        print(f"Youth tickets are: ${bill}")
    elif age > 18:
        bill += 12
        print(f"Adult tickets are: ${bill}")
    elif (age > 45) and (age < 50):
        bill += 0
        print("Everything will be alright, you have a free ride on the house")
else:
    print("Cannot ride on the rollercoaster")
 
photo = input("Do you want to take a photo? Y or N. ")
if photo == "Y":
    bill += 3
    print(f"Your total bill is: ${bill}")
else:
    print("Your total bill is: ${bill}")
