# Zadanie:

# Zaimplementuj prostą grę zgadywania liczby z wykorzystaniem biblioteki random i wczytaniem listy słów z pliku txt.
# Użytkownik będzie zgadywał liczbę, a po odgadnięci co wybrał komputer program wyświetli jakie słowo pod tą liczbą się kryje.
# Program zapyta użytkownika czy chce zagrać jeszcze raz i ponownie wylosuje nowe słowo z pliku tekstowego do odgadnięcia!

import random


# 1. PROGRAM WYBIERA LICZBE:
def choose_number():
    number = random.randrange(1, 31)
    return number


# 2. GRACZ ZGADUJE LICZBE:
def guess_number():
    print('Zgadnij liczbe, o ktorej mysle! Od 1 and 30! ')
    user_number = int(input())

    while number != user_number:
        # Here goes the added part of code:
        if user_number > number:
            print('Nie! Ta liczba jest za wysoka. Sprobuj jeszcze raz: ')
        else:
            print('Nie! Ta liczna jest za mala. Sprobuj jeszcze raz: ')
        # The end of the added part.
        user_number = int(input())

    print('WYMIATASZ! TO POPRAWNA LICZBA!')


# 3. PROGRAM WCZYTUJE PLIK TEKSTOWY I TWORZY LISTE SLOW:
def check_number():
    wordlist = []  # Tworze pusta liste.
    words = open('words.txt', 'r')  # Otwieram plik ze slowami. TU POWINNA BYC POPRAWNA CALA SCIEZKA.
    for line in words:  # Dla kazdej linijki ('line') w pliku ze slowami ('words') program wyizolowuje pojedyncze linie/slowa ("line.strip") i kazde slowo dodaje do listy ("list.append")
        wordlist.append(line.strip())

    # 4. PROGRAM NUMERUJE ELEMENTY LISTY:
    list_number = int(number) - 1
    print('Pod numerem ' + str(number) + ' kryje sie slowo: ' + wordlist[list_number])


# 5. PROGRAM PYTA CZY GRACZ CHCE ZAGRAC JESZCZE RAZ I EWENTUALNIE POWTARZA GRE.
def play_again():
    print('Czy chcesz zagrac jeszcze raz? tak/nie')
    answer = input()
    if answer == 'tak':
        choose_number()
        guess_number()
        check_number()
        play_again()
    else:
        quit()


choose_number()
number = choose_number()
guess_number()
check_number()
play_again()