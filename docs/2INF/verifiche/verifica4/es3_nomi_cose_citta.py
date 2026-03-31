from random import choices
from string import ascii_uppercase

def random_letters(n):
    """Genera una lista con n lettere maiuscole casuali"""
    return choices(ascii_uppercase, k=n)

def starts_with(text, letter):
    """
    Restituisce True se un testo comincia con una lettera,
    False in caso contrario. Ignora maiuscole e minuscole.
    """
    return text.upper().startswith(letter)

# Nomi-Cose-Città
# ---------------

# Giochiamo con 5 lettere a caso. Per ogni lettera, chiediamo all'utente
# di inserire una parola (un nome, una cosa, una città) che cominci con
# quella lettera.

# 1. scrivere una funzione ask(what, letter) che chiede all'utente
#    una parola di un certo tipo (what: nome, cosa, città) e verifichi
#    che questa cominci con la lettera (letter) scelta.
#    Usare la funzione starts_with (vedi sopra) per fare questa verifica.
#    Se l'utente inserisce una parola che non comincia
#    con la lettera giusta, ripetere la domanda.

def ask(what, letter):
    text = input(f"Dammi un {what} con la {letter}:")
    while not starts_with(text, letter):
        text = input(f"Deve cominciare con la {letter}:")
    return text

# 2. Per ogni lettera del gioco (ne vogliamo 5 a caso) chiedere all'utente
#    un nome, una cosa e una città utilizzando la funzione ask del punto 1.
#    Usiamo la funzione random_letters (vedi sopra) per scegliere 5 lettere a caso.
#    Stampare in una riga cosa ha inserito l'utente
#    e poi passare alla lettera successiva.

# Esempio:

# È uscita la S
# Un nome con la S? ...
# Una cosa con la S? ...
# Una città con la S? ...
# Hai detto: Sxxx, Syyy, Szzz
# È uscita la F
# Un nome con la F?
# ...

for letter in random_letters(5):
    print(f"È uscita la {letter}")
    nome = ask("Nome", letter)
    cosa = ask("Cosa", letter)
    citta = ask("Città", letter)
    print(f"Hai detto: {nome}, {cosa}, {citta}")