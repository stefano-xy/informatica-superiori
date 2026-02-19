---
title: Esempi Python
parent: 2INF
layout: page
nav_order: 6
---

# Esempi di codice Python

Alcune esercizi con _Python_ spiegati.

1. TOC
{: toc }

Possiamo scrivere e verificare questi programmi su:

- [FARE](https://fare.polito.it/python), ambiente del Politecnico di Torino.
- [Online GDB](https://www.onlinegdb.com), ricordandoci di selezionare _Python 3_ da menù in alto a destra.

## Numeri primi

In questo esempio vogliamo calcolare e stampare dei numeri primi.
Definizione: un numero è primo se è divisibile solo per 1 e per sé stesso.

Per verificare se un numero `a` è divisibile per un numero `b`, usiamo
l'operatore _modulo_ (`%`) che calcola il resto della divisione di `a` per `b`.
Verifichiamo se `b` è divisore di `a` controllando se `a % b == 0`.

In generale, per un numero `n` se non si trova un divisore fra `2` e `n - 1`, allora `n` è primo.

Esistono algoritmi sicuramente più complessi e efficienti per verificare
se un numero è primo ma noi useremo questo algoritmo semplice. I numeri
primi sono fondamentali in matematica e informatica, in particolare per la crittografia:
c'è tanto tanto lavoro universitario e di centri di ricerca ma a noi _va bene così_.

Separiamo allora l'esercizio in più parti.

### Controllare se un numero è primo

Chiediamo all'utente un numero `n` e verifichiamo se è primo:

```python
n = int(input("Inserisci un numero"))

# Il numero è primo fino a prova contraria
is_prime = True

# Cerchiamo quindi le prove contrarie, cerchiamo cioè
# se esiste almeno un divisore fra 2 e n - 1.
for d in range(2, n): # range(2, n) esclude n
  if n % d == 0:      # se d è divisore di n
    is_prime = False  # allora n non è primo
    break             # Non è necessario, ma leggi sotto

# Stampiamo il risultato
if is_prime:
  print(n, "è primo")
else:
  print(n, "non è primo")
```

Il cuore dell'algoritmo, il ciclo `for`, ricerca i potenziali divisori `d`
nell'intervallo fra `2` e `n - 1`, usando `range(2, n)` che include
nell'intervallo il 2 ma non include l'_n_.

L'istruzione `break` serve per abbreviare il calcolo. Avendo trovato
un divisore, non ha senso continuare a cercare quindi `break` blocca
il ciclo `for` prima che questo si concluda. Non è essenziale farlo.

### Stampa dei numeri primi fino a 1000

Capito come si controlla se un numero è primo o meno, possiamo
usare il cuore dell'esempio precedente per stampare tutti i numeri
primi che si trovano fino a 1000. Non serve più chiedere all'utente niente.

```python
for n in range(2, 1000 + 1): # andiamo a cercare i numero fino a 1000 incluso
  is_prime = True
  for d in range(2, n): # range(2, n) esclude n
    if n % d == 0:
      is_prime = False
      break
  if is_prime:
    print(n)
```

Vediamo che il numero primo più grande prima di 1000 è **997**.

### Stampa dei primi 1000 numeri primi

Un'altra variante potrebbe essere quella di stampare
tutti i numeri primi finché non se ne trovino 1000.

Usiamo un `while` e contiamo quanti ne troviamo.
Non possiamo usare un `for` perché non sappiamo questi
1000 numeri quali sono e quindi fino a che numero cercare.

```python
found = 0 # qui contiamo quanti ne abbiamo trovati
n = 2     # partiamo da 2

# Andiamo alla ricerca fino a quando non ne troviamo 1000
while found < 1000:

  # Verifichiamo n
  is_prime = True
  for d in range(2, n): # range(2, n) esclude n
    if n % d == 0:
      is_prime = False
      break

  # n è primo, segnamocelo
  if is_prime:
    found = found + 1
    print(n)
  
  # Prossimo n
  n = n + 1
```

Ci mette un po' perché troveremo che il millesimo numero primo è **7919**.
Più un numero è grande e più ci mette a fare il controllo.

Vedete quanto ci mette e poi provate a vedere quanto ci mette senza `break`.
Vedrete che ci impiegherà _molto_ di più.

## Tavola pitagorica

Vogliamo generare una tavola pitagorica 10x10, dove sono rappresentate
tutte le tabelline da 1 a 10, cioè tutte le possibili moltiplicazioni
fra i numeri da 1 a 10.

![](tavola_pitagorica.jpg)

Non vogliamo una tabella con tutti i bordi e i colori, ma semplicemente
i numeri a formare un quadrato, possibilmente incolonnati bene.
Non vogliamo neanche le righe e le colonne con lo zero.

Per ogni numero `x` e `y` compreso fra 1 e 10, vogliamo stampare il loro prodotto.

La frase precedente può essere quasi trascritta in _Python_ direttamente:

```python
for x in range(1, 11): # fino a 10, cioè 11 escluso
  for y in range(1, 11):
    print(x * y)
```

Questo stampa un elenco di 100 numeri. Miglioriamo l'esercizio andando a capo
correttamente, solo alla fine cioè di ogni riga:

```python
for x in range(1, 11):    # fino a 10, cioè 11 escluso
  for y in range(1, 11):
    print(x * y, end=" ") # non va a capo ma lascia uno spazio
  print()                 # va a capo
```

Il parametro `end=" "` fa si che invece di terminare la stampa del numero
andando a capo, come normalmente avviene, si aggiunge uno spazio. Così facendo
i numeri non vengono più stampati in un'unico elenco, ma in un'unica riga.
Aggiungendo poi il secondo `print()` a fine di ogni riga, cioè alla fine
di ogni ciclo `for` esterno, questo va a capo.

Si forma una tabella 10x10 di numeri, sebbene non incolonnata benissimo
in quanto i numeri minori di 10 occupano un solo carattere invece che 2
rendendo la tabella _ammaccata_.

Proviamo a risolverlo così:

```python
for x in range(1, 11):    # fino a 10, cioè 11 escluso
  for y in range(1, 11):
    n = x * y
    if n < 10:
      print("", end=" ")  # stampa uno spazio e non va a capo
    print(n, end=" ")     # non va a capo ma lascia uno spazio
  print()                 # va a capo
```

Che produce questo risultato:

```
 1  2  3  4  5  6  7  8  9 10 
 2  4  6  8 10 12 14 16 18 20 
 3  6  9 12 15 18 21 24 27 30 
 4  8 12 16 20 24 28 32 36 40 
 5 10 15 20 25 30 35 40 45 50 
 6 12 18 24 30 36 42 48 54 60 
 7 14 21 28 35 42 49 56 63 70 
 8 16 24 32 40 48 56 64 72 80 
 9 18 27 36 45 54 63 72 81 90 
10 20 30 40 50 60 70 80 90 100 
```

## Roulette

Simuliamo il lancio della pallina della [roulette](https://it.wikipedia.org/wiki/Roulette):

![](roulette1.jpg)

Al casinò, nel gioco della roulette, il _[croupier](https://it.wikipedia.org/wiki/Croupier)_
lancia una pallina mentre la ruota è in movimento e pronuncia le frasi _Les jeux sont faits!_
e poi _Rien ne va plus!_ per dire i giochi e tutte le puntate sono finite: si aspetta il risultato.

La roulette è un gioco francese e le frasi ufficiali sono quindi tutte in francese.

Quando la pallina e la ruota si fermano, il _croupier_ annuncia il risultato descrivendo
le caratteristiche del numero uscito, ad esempio dicendo _27 : rouge, impair et passe_.
Può uscire un numero a caso da zero a 36.

![](roulette2.png)

Simuliamo il lancio della pallina della roulette in questo modo:

- Generiamo un numero a caso da 0 a 36.
- Dire se il numero uscito è zero oppure no.
- Se è uscito zero, non c'è altro da aggiungere.
- Se non è uscito zero:
  - Dire quale numero è uscito
  - Dire se il numero uscito è rosso (_rouge_) o nero (_noir_)
  - Dire se il numero uscito è pari (_pair_) o dispari (_impair_)
  - Dire se il numero uscito è minore o uguale a 18 (_manque_) o maggiore di 18 (_passe_)

I numeri rossi sono 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34 e 36.
Gli altri sono neri. Lo zero è verde.

_Hint:_ per generare un numero casuale, seguire le istruzioni della documentazione di python:

```
random.randint(a, b)
Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
```

Bisogna importare la funzione `randint` per poterla usare tramite `from random import randint`.

Prima possibile soluzione:

```python
# Per poter usare la funzione randint dobbiamo "prenderla" (importarla) dal modulo random
from random import randint

print("Les jeux sont faits!")
print("Rien ne va plus!")

# Tiriamo la pallina, esce un numero
n = randint(0, 36)

if n == 0:
  print("Zero!")
else:
  # Stampa il numero
  print(n)
  
  # Stampa se rosso o nero
  if n in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
    print("Rouge")
  else:
    print("Noir")
    
  # Stampa se pari o dispari
  if n % 2 == 0:
    print("Pair")
  else:
    print("Impair")  
 
  # Stampa se maggiore o minore di 18
  if n <= 18:
    print("Manque")
  else:
    print("Passe")
```

Una versione migliore, che separa il calcolo dalla stampa dei messaggi:

```python
# Per poter usare la funzione randint dobbiamo "prenderla" (importarla) dal modulo random
from random import randint

print("Les jeux sont faits!")
print("Rien ne va plus!")

# Qui calcoliamo tutto
n = randint(0, 36)
is_zero = n == 0
is_red = n in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
is_even = n % 2 == 0
is_low = n <= 18

# Qui stampiamo senza fare alcun calcolo
if is_zero:
  print("Zero!")
else:
  # Stampa il numero
  print(n)
  
  # Stampa se rosso o nero
  if is_red:
    print("Rouge")
  else:
    print("Noir")

  # Stampa se pari o dispari
  if is_even:
    print("Pair")
  else:
    print("Impair")
  
  # Stampa se maggiore o minore di 18
  if is_low:
    print("Manque")
  else:
    print("Passe")
```

Abbiamo introdotto delle variabili booleane che iniziano, per convenzione,
con `is_` e indicano una proprietà che può essere vera (`True`) o falsa (`False`):

- `is_zero` per indicare se il numero uscito è zero
- `is_red` per indicare se è rosso
- `is_even` per indicare se è pari
- `is_low` per indicare se è minore o uguale a 18

{: .highlight }
Avendo separato il calcolo dalla stampa, possiamo riscrivere la parte che stampa i messaggi
tante volte senza doverci preoccupare di cambiare come il risultato viene calcolato.
_Separare 2 funzionalità in 2 pezzi di codice distinti_ è sempre un bene.

Stessa versione ancora più elegante, facendo uso della sistassi compatta (tecnica avanzata!) `x if condizione else y`:

```python
# Per poter usare la funzione randint dobbiamo "prenderla" (importarla) dal modulo random
from random import randint

print("Les jeux sont faits!")
print("Rien ne va plus!")

# Qui calcoliamo tutto
n = randint(0, 36)
is_zero = n == 0
is_red = n in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
is_even = n % 2 == 0
is_low = n <= 18

# Qui stampiamo senza fare alcun calcolo
if is_zero:
  print("Zero!")
else:
  # Stampa il numero
  print(n)
  
  # Stampa se rosso o nero
  print("Rouge" if is_red else "Noir")

  # Stampa se pari o dispari
  print("Pair" if is_even else "Impair")
    
  # Stampa se maggiore o minore di 18
  print("Manque" if is_low else "Passe")
```

Finale ancora migliore, formattiamo meglio tutto in un'unica frase:

```python
# Per poter usare la funzione randint dobbiamo "prenderla" (importarla) dal modulo random
from random import randint

print("Les jeux sont faits!")
print("Rien ne va plus!")

# Qui calcoliamo tutto
n = randint(0, 36)
is_zero = n == 0
is_red = n in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
is_even = n % 2 == 0
is_low = n <= 18

# Qui stampiamo senza fare alcun calcolo
if is_zero:
  print("Zero!")
else:
  # Stampa la frase che annuncia il numero
  print(n,
    ":",
    "rouge," if is_red else "noir,",
    "pair" if is_even else "impair",
    "et",
    "manque" if is_low else "passe")
```

## 7 e mezzo

Simuliamo [7 e mezzo](https://it.wikipedia.org/wiki/Sette_e_mezzo), il gioco di carte.
Il banco chiede al giocatore se vuole una carta e si ripete finché
il giocatore non dice _basta_ oppure sballa, cioè accumula più punti di 7 e mezzo.

Queste le regole del gioco semplificate:

- Al giocatore si chiede se vuole una carta.
- Se esce una carta semplice, da 1 (asso) a 7, questi sono
  i punti che il giocatore accumula.
- Se esce una figura: 8 (fante), 9 (cavallo) o 10 (re)
  il giocatore accumula 0,5 punti.
- Se il giocatore raggiunge esattamente 7,5 ha vinto.
- Se il giocatore supera 7,5 ha perso.
- Altrimenti il giocatore può chiedere un'altra carta
  o fermarsi al punteggio che ha accumulato.

Il gioco vero è più complicato, ha il re di denari, ma noi facciamo una
versione semplificata che non ha i semi ma ha solo carte semplici da 1 a 10.

Una possibile soluzione può essere:

```python
# 7 e mezzo
from random import randint
punti = 0

# Chiedi al giocatore se vuole una carta
while input("Carta? ") in ["si", "sì", "Sì", "Si"]:
    
  carta = randint(1, 10) # pesca una carta da 1 a 10
  print("Hai pescato", carta)
  
  if carta in [8, 9, 10]: # è una figura
    punti = punti + 0.5
  else:
    punti = punti + carta
    
  print("Hai", punti, "punti")
  
  if punti == 7.5:
    print("Hai vinto, 7 e mezzo!")
    break # interrompi il while perchè hai vinto
  elif punti > 7.5:
    print("Hai sballato e hai perso!")
    break # interrompi il while perchè hai perso

print("Hai fatto", punti, "punti")
```