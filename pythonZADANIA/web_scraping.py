"""Zadanie 1:
W ramach rozgrzewki zastanów się jak wyciągniesz informacje z poniższej zmiennej
(ten fragment kodu dobrze wyświetli sie tylko w przeglądrce na komputerze)
html_input = "<ul><li>Jabłko</li><li>Gruszka</li><li>Pomarańcza</li></ul>"
(ten fragment kodu dobrze wyświetli sie tylko w przeglądrce na komputerze)

Twoim zadaniem jest użyć Pythona i odpowiednich metod typu string, aby wyodrębnić tylko tekst z wnętrza znaczników <li>, a następnie zapisać go jako listę:

['Jabłko', 'Gruszka', 'Pomarańcza']"""

html_input = "<ul><li>Jabłko</li><li>Gruszka</li><li>Pomarańcza</li></ul>"

remove_list = ['<ul>', '</li>', '</ul>']

for i in remove_list:
    html_input = html_input.replace(i, '')

lista = html_input.split('<li>')

nowa_lista = []

for n in lista:
    if len(n) > 0:
        nowa_lista.append(n)

print(nowa_lista)