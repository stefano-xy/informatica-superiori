---
title: Esercitazioni + soluzioni
parent: 2INF
layout: page
nav_order: 9
---

# Esercitazioni con soluzioni allegate

Alcune esercitazioni su _Flowrun_ e _python_ con soluzioni allegate (da scaricare).

1. TOC
{: toc }

## Esercitazioni parte 1

### La persona più grande

Scrivere con [Flowrun](https://www.flowrun.io) un algoritmo che chieda agli utenti 5 nomi e la loro età.
Es: _Come ti chiami?_, _Quanti anni hai?_ ... ripetuto 5 volte.

Alla fine, stampare il nome della persona più grande e quanti anni questa ha.

Bonus: nella seconda domanda, ripetere il nome dell'utente. Es:
- _Come ti chiami?_ Giovanni
- _Giovanni, quanti anni hai?_ 18

[Soluzione](parte1/es1_max_age.flowrun){: .btn }

### Contare fino a N

Scrivere con [Flowrun](https://www.flowrun.io) un algoritmo che chieda all'utente un numero
e stampi poi tutti i numeri da 1 a quel numero inserito.

[Soluzione](parte1/es2_count_n.flowrun){: .btn }

### Patenti di guida

Scrivere con [Flowrun](https://www.flowrun.io) un algoritmo con questi passaggi:

- Chiedere l'età dell'utente
- Scrivere se può guidare il motorino (da 14 anni)
- Scrivere se può guidare una moto 125 (da 16 anni)
- Scrivere se può guidare un'auto (da 18 anni)
- Scrivere se può andare a piedi (indipendentemente dall'età)

### Ripeti fino a zero

Scrivere con [Flowrun](https://www.flowrun.io) un algoritmo con questi passaggi:

- Salutare con il messaggio _Buongiorno, inserisci un numero_.
- Chiedere all'utente un numero.
- Ripetere i passi seguenti fino a quando l'utente non inserisce zero.
- Scrivere il messaggio _Riprova_.
- Chiedere un altro numero.
- A fine ripetizione, salutare con il messaggio _Grazie, ciao_.

[Soluzione](parte1/es4_ripeti_fino_a_zero.flowrun){: .btn }

### Calcolo del massimo

Continuazione dell'esercizio precedente.

Scrivere con [Flowrun](https://www.flowrun.io) un algoritmo con questi passaggi:

- Salutare con il messaggio _Buongiorno, inserisci un numero_.
- Chiedere all'utente un numero.
- Ripetere i passi seguenti fino a quando l'utente non inserisce zero.
- Scrivere il messaggio _Riprova_.
- Chiedere un altro numero.

A fine ripetizione:
- Scrivere il numero più grande fra tutti quelli inseriti.
- Salutare con il messaggio _Grazie, ciao_.
- Salvarlo come file e allegarlo alla soluzione.

Suggerimento: servirà una variabile dove tener traccia del numero più grande inserito fino a quel momento.

Bonus: complicare l'esercizio calcolando anche il minimo, il numero di numeri inseriti
e la somma dei numeri inseriti. A fine ripetizione stampare tutti questi dati.

[Soluzione](parte1/es5_calcolo_max.flowrun){: .btn .mr-2 }
[Soluzione + Bonus](parte1/es5_calcolo_max_min_sum_count.flowrun){: .btn }

### Numeri crescenti o decrescenti

Scrivere con [Flowrun](https://www.flowrun.io) un algoritmo con questi passaggi:

Chiedere all’utente 3 numeri.
- Se i numeri vengono dati in ordine crescente, cioè se ogni numero è maggiore del precedente, scrivere _Numeri in ordine crescente_.
- Se i numeri vengono dati in ordine decrescente, cioè se ogni numero è minore del precedente, scrivere _Numeri in ordine decrescente_.
- Se i numeri sono tutti uguali, scrivere _Numeri tutti uguali_.
Altrimenti scrivere _Numeri in nessun ordine particolare_.

[Soluzione](parte1/es6_crescenti_decrescenti.flowrun){: .btn }