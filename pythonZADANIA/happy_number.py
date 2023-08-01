# "Zadanie: Napisz skrypt "Szczęśliwy numerek"

# Skrypt losuje nr od 1 do 30.
# Następnie wyświetli napis "Szczęśliwy numer to {numer}.
# Dzisiaj nauczyciel nie może Cię odpytać na lekcji! Super!""


import random

def happy_number():
    return random.randint(1,31)

print(f"Szczęśliwy numer to {happy_number()} Dzisiaj nauczyciel nie może Cię odpytać na lekcji! Super!")


