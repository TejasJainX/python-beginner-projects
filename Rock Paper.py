import random


random_number = random.randint(1, 3)
if random_number == 1:
    computer = "Rock"
elif random_number == 2:
    computer = "Paper"
elif random_number == 3:
    computer = "Scissor"

while True:
    generator = input("Rock, Paper, Scissors? (r/p/s): ")

    random_number = random.randint(1, 3)
    if random_number == 1:
        computer = "Rock"
    elif random_number == 2:
        computer = "Paper"
    elif random_number == 3:
        computer = "Scissor"
    if generator.lower() != 'r' and generator.lower() != 'p' and generator.lower() != 's':
        print('Invalid choice!')
    elif generator.lower() == 'r':
        print('You chose Rock!')
        print(f"Computer choose {computer}")
        if computer == "Rock":
            print('Tie')
            continue
        elif computer == "Paper":
            print('You win')
            continue
        elif computer == "Scissor":
            print('You lose')
            continue
    elif generator.lower() == 'p':
        print('You chose Rock!')
        print(f"Computer choose {computer}")
        if computer == "Rock":
            print('Tie')
            continue
        elif computer == "Paper":
            print('You win')
            continue
        elif computer == "Scissor":
            print('You lose')
            continue
    elif generator.lower() == 's':
        print('You chose Rock!')
        print(f"Computer choose {computer}")
        if computer == "Rock":
            print('Tie')
            continue
        elif computer == "Paper":
            print('You win')
            continue
        elif computer == "Scissor":
            print('You lose')
            continue


INCOMPLETE


# REMOVED INLINE SUGGEST TO DO ON MY OWN
