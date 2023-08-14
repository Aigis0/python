height = float(input("what is your height in m: "))
weight = float(input("what is your weight in kg: "))
bmi = round(weight / height ** 2)

if bmi <= 18.5:
    print(f"your bmi is {bmi} and you are underweight")
elif bmi <= 25:
    print(f"your bmi is {bmi} and you have a normal weight")    
elif bmi <= 30:
    print(f"your bmi is {bmi} and you are slightly overweight ")
elif bmi <= 35:
    print(f"your bmi is {bmi} and you are obese")
else:
    print(f"your bmi is {bmi} and you are clinically obese")
