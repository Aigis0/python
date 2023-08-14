import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, seperated by a comma: ")
names = namesAsCSV.split(", ")
random_number = len(names)
random_name = random.randint(0, random_number - 1)
bill = names[random_name]
print(f"{bill} is going to pay the bill")
