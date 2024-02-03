import random
user_score = computer_score = 0
computer_choice = random.randint(1, 3)
running = True
choice_list = ['tie', 'Rock', 'Paper', 'Scissors']

def display_user_choice(choice):
    if choice == 1:
        print("User's choice is rock")
    elif choice == 2:
        print("User's choice is paper")
    elif choice == 3:
        print("User's choice is scissor")


def display_comp_choice(computer_choice):
    if computer_choice == 1:
        print("Computer's choice is rock")
    elif computer_choice == 2:
        print("Computer's choice is paper")
    elif computer_choice == 3:
        print("Computer's choice is scissor")


def start(user_score, computer_score):
    while running:
        try:
            for choice in choice_list:
                choice = int(input("Enter 1 for Rock, 2 for Paper and 3 for Scissors: "))
                display_user_choice(choice)
                display_comp_choice(computer_choice)
                if choice not in range(1,3):
                    print('Invalid. Try again')
                if choice == computer_choice:
                    user_score += 0
                    computer_score += 0
                    print(f"Both user and computer has the same choice. Result: It's a tie",
                            '\nUser score:', user_score, 'Computer score:', computer_score)

                elif choice == 1 and computer_choice == 2:
                    computer_score += 1
                    user_score += 0
                    print('Result: Computer wins',
                            '\nUser score:', user_score, 'Computer score:', computer_score)

                elif choice == 2 and computer_choice == 1:
                    user_score += 1
                    computer_score += 0
                    print(f"Result: User wins",
                            '\nUser score:', user_score, 'Computer score:', computer_score)

                elif choice == 1 and computer_choice == 3:
                    user_score += 1
                    computer_score += 0
                    print(f"Result: User wins",
                            '\nUser score:', user_score, 'Computer score:', computer_score)

                elif choice == 3 and computer_choice == 1:
                    computer_score += 1
                    user_score += 0
                    print(f"Result: Computer wins",
                            '\nUser score:', user_score, 'Computer score:', computer_score)

                elif choice == 2 and computer_choice == 3:
                    computer_score += 1
                    user_score += 0
                    print(f"Result: Computer wins",
                            '\nUser score:', user_score, 'Computer score:', computer_score)

                elif choice == 3 and computer_choice == 2:
                    user_score += 1
                    computer_score += 0
                    print(f"Result: User wins",
                            '\nUser score:', user_score, 'Computer score:', computer_score)
                if user_score == 2 or computer_score == 2:
                    print("End game")
                    if user_score == 2:
                        print('User won')
                    else:
                        print('Computer won')
                    print('Good Bye!')
                    exit()
                break
        except ValueError:
            print('Invalid')


def main():
    start(user_score, computer_score)
    display_user_choice(choice)
    display_comp_choice(computer_choice)



main()
