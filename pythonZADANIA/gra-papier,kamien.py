# Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.
# Write rock-paper-scissors so as to use the function

import random

def get_user_choice():
    return input('Wybierz kamień, papier lub nożyce: ')

def get_computer_choice():
    choices = ['kamień', 'papier', 'nożyce']
    return random.choice(choices)

def play(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "REMIS! Zagraj jeszcze raz, żeby wygrać"

    elif (user_choice == 'kamień' and computer_choice == 'nożyce') or \
         (user_choice == 'papier' and computer_choice == 'kamień') or \
         (user_choice == 'nożyce' and computer_choice == 'papier'):
        return 'Wygrywasz!'
    else:
        return 'Przegrywasz!'

def play_again():
    play_again = input('Czy chcesz zagrać jeszcze raz? (tak/nie):' )
    if play_again.lower() == 'tak':
        return True
    else:
        return False

def main():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = play(user_choice, computer_choice)
        print(f'Komputer wybrał: {computer_choice}')
        print(result)
        if not play_again():
            break

if __name__ == "__main__":
    main()
