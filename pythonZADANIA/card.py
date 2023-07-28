# 2. Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
# Co wiemy o tych numerach tych kart?
# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
# # American Express card numbers start with 34 or 37 and have 15 digits.




def check_card_type(card_number):
    card_number = str(card_number)
    if card_number.startswith('4'):
        if len(card_number) == 13 or len(card_number) == 16:
            return "Visa"
    elif card_number.startswith(('51', '52', '53', '54', '55')) or (2221 <= int(card_number[:4]) <= 2720):
        if len(card_number) == 16:
            return "MasterCard"
    elif card_number.startswith(('34', '37')):
        if len(card_number) == 15:
            return "American Express"
    return "Unknown"

def main():
    card_number = input("Podaj numer karty: ")
    card_type = check_card_type(card_number)
    print(f"Typ karty: {card_type}")

if __name__ == "__main__":
    main()