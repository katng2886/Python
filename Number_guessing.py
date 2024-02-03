import random
keepplaying = True
user_score = 0
computer_score = 0
i = 0
while keepplaying:
    for i in range(1, 20):
        i += 1
        user = random.randint(1, 100)
        computer = random.randint(1, 100)
        print("This is user number: ", user)
        user_guess = input("Do you think your number is higher or lower than the computer's number (higher/lower): ")
        if user_guess == 'higher':
            if computer < user:
                print(f'\nComputer number is: {computer}')
                user_score += 1
                computer += 0
                print(f"\nYou are correct, \nuser scored: {user_score} \ncomputer scored: {computer_score}")
            else:
                print(f'\nComputer number is: {computer}')
                computer_score += 1
                print(f"\nYou are incorrect, \nuser scored: {user_score} \ncomputer scored: {computer_score} ")
        if user_guess == 'lower':
            if computer < user:
                print(f'\nComputer number is: {computer}')
                computer_score += 1
                print(f'\nYou are incorrect, \nuser scored: {user_score} \ncomputer scored: {computer_score} ')
            else:
                print(f'\nComputer number is: {computer}')
                user_score += 1
                print(f'\nYou are incorrect, \nuser scored: {user_score} \ncomputer scored: {computer_score}')
            i += 1
        if user_score == 10 or computer_score == 10:
            print("End game")
            if user_score > computer_score:
                print(f"User wins, user scored: {user_score} ")
            else:
                print(f"Computer wins, computer scored: {computer_score}")
            break
    break

