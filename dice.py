import random

print("This is a dice simulator!")

again = 'y'
while (again == 'y'):
    x = random.randint(1, 7)
    if (x == 1):
        print("---------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("---------")
    elif (x == 2):
        print("---------")
        print("|       |")
        print("| O   O |")
        print("|       |")
        print("---------")
    elif (x == 3):
        print("---------")
        print("|   O   |")
        print("|   O   |")
        print("|   O   |")
        print("---------")
    elif (x == 4):
        print("---------")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print("---------")
    elif (x == 5):
        print("---------")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print("---------")
    elif (x == 6):
        print("---------")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print("---------")
    again = input("Press y to roll again : ")