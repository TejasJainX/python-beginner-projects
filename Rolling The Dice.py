import random

dice = input("Roll the dice? (y/n): ")
while True:
    if dice.lower() == 'y':
        A = random.randint(1, 6)
        B = random.randint(1, 6)
        print(f"({A}, {B})")
        dice = input("Roll the dice? (y/n): ")
    elif dice.lower() == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')
        dice = input("Roll the dice? (y/n): ")
        continue

# TRIAL 1

# while (dice1.lower() != "n" or dice1.lower() == "y") and True:
#     if dice1.lower() != 'n' and dice1.lower() != 'y':
#         print('Invalid choice!')
#         dice2 = input("Roll the dice? (y/n): ")
#         A = random.randint(1, 6)
#         B = random.randint(1, 6)
#         print(f"({A}, {B})")
#         dice = input("Roll the dice? (y/n): ")
#     elif dice.lower() == 'y':
#         X = random.randint(1, 6)
#         Y = random.randint(1, 6)
#         print(f"({X}, {Y})")
#         dice = input("Roll the dice? (y/n): ")
#     elif dice.lower() == 'n':
#         print('Thanks for playing!')
#         break

