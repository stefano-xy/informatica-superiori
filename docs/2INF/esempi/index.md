---
title: Esempi
parent: 2INF
layout: page
nav_order: 6
---

# Esempi di codice Python

Alcune esercitazioni su _Flowrun_ e _python_ con soluzioni allegate (da scaricare).

1. TOC
{: toc }

## Numeri primi

_(in via di pubblicazione)_

## Tavola pitagorica

_(in via di pubblicazione)_

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
