---
title: Verifiche + soluzioni
parent: 2INF
layout: page
nav_order: 10
---

# Verifiche con soluzioni allegate

Alcune proposte da utilizzare per le verifiche.

1. TOC
{: toc }

## Pre-verifica sul sistema di numerazione binario

Mostrare tutti i passaggi intermedi.

1. [Convertire da binario a decimale](../binario/index.md#da-binario-a-decimale) 3 numeri a scelta:

   - 4 cifre, di cui almeno 3 _uno_
   - 6 cifre, di cui almeno 4 _uno_
   - 8 cifre, di cui almeno 5 _uno_

2. [Convertire da decimale a binario](../binario/index.md#da-decimale-a-binario) 3 numeri a scelta:

   - Primo numero da 10 a 50
   - Secondo numero da 10 a 250
   - Terzo numero da 250 a 500

   Effettuare la prova, convertendo i numeri binari trovati
   di nuovo in decimale, verificando che i conti tornino.

3. Scegliere 2 numeri binari a piacere, 6-8 cifre.

   [Calcolare la somma](../binario/index.md#somma-fra-numeri-binari) in binario.
   Convertire tutti i numeri in decimale.
   Verificare che la somma in decimale corrisponda a quella in binario.

## Verifica 1: sistemi di numerazione

Mostrare tutti i passaggi intermedi.

1. Scegliere 2 numeri binari a piacere da 10 cifre.
   [Calcolare la somma](../binario/index.md#somma-fra-numeri-binari) in binario.
   Convertire tutti i numeri in decimale.
   Verificare che la somma in decimale corrisponda a quella in binario.

2. [Contare in esadecimale](../esadecimale/index.md#contare-in-esadecimale). Prendere come numero di partenza
   il giorno del vostro compleanno e interpretarlo come numero esadecimale.

   Es. 18/4/2006 -> 0x18 = 18 esadecimale

   Partendo da questo numero, scrivere i 20 numeri che seguono, in esadecimale:
   `18 19 1A 1B ...`

3. [Convertire da esadecimale a decimale](../esadecimale/index.md#da-esadecimale-a-decimale) 2 numeri a scelta:

   - 2 cifre, di cui almeno 1 _lettera_
   - 3 cifre, di cui almeno 2 _lettere_

4. [Convertire da decimale a esadecimale](../esadecimale/index.md#da-decimale-a-esadecimale) 2 numeri a scelta:

   - Primo numero da 500 a 1000
   - Secondo numero da 1000 a 5000

   Effettuare la prova, convertendo i numeri esadecimali trovati
   di nuovo in decimale, verificando che i conti tornino.

5. Di che [colori RGB](../codifiche/index.md#codifica-dei-colori-rgb) stiamo parlando? Come si riesce a capire che colori sono?

   - #2A0FE9
   - #8A0F79
   - #FFA002

6. Codificare in _byte_ la stringa `È così facile, no?`.
   È possibile [codificarla in ASCII](../codifiche/index.md#codifica-di-testo-ascii)? Sì o no? Motivare la risposta.
   È possibile [codificarla in UTF-8](../codifiche/index.md#codifica-di-testo-unicode)? Usare [unicode.run](https://unicode.run/).
   Spiegare il significato di ogni _byte_ della codifica UTF-8.

   La risposta alla domanda è: `50 69 C3 B9 20 6F 20 6D 65 6E 6F`.
   Quale è il testo corrispondente?

## Verifica 2a: algoritmi e diagrammi

Risolvere con [FlowRun](https://www.flowrun.io).

1. Anagrafica (facile)

   Chiedere all'utente il proprio nome, comune di nascita e l'anno di nascita.
   Calcolare quanti anni ha l'utente: siamo nel 2025 quindi ...
   Stampare il messaggio _NOME, sei nato a XX e hai YY anni_ dove al posto di `NOME`, `XX` e `YY` dovrà esserci
   il nome dell'utente, il suo comune di nascita e la sua età.

   [Soluzione](verifica2a/es1_anagrafica.flowrun){: .btn }

2. Indovina un numero (medio)

   Il sistema pensa un numero a caso da 0 a 100. Per fare questo, definire una variabile intero e
   inizializzarla con l'espressione `randomInt(100)`.
   L'utente ha più tentativi per indovinare questo numero.
   Ogni volta che l'utente inserisce un numero che non corrisponde, il sistema di dice _Riprova, deve essere più grande_
   oppure _Riprova, deve essere più piccolo_ e gli viene data la possibilità di riprovare, all'infinito.
   Quando l'utente inserisce il numero corretto, il sistema dice _Bravo, hai indovinato_ e il gioco si ferma.

   [Soluzione](verifica2a/es2_indovina.flowrun){: .btn }

3. Che ore sono? (difficile)

   Chiedere all'utente che ore sono (`hh:mm`). L'utente risponderà inserendo le ore (`hh`) e i minuti (`mm`) separatamente.
   Ringraziare e salutare poi l'utente in questo modo:
   
   - _Grazie, buona giornata!_ dalle ore 06:00 alle ore 12:00.
   - _Grazie, buon pomeriggio!_ dalle ore 12:00 alle ore 17:30.
   - _Grazie, buona serata!_ dalle are 17:30 alle are 22:30.
   - _Grazie, buona notte!_ nei restanti orari, cioè prima delle 06:00 e dopo le 22:30.

   Cosa fare esattamente all'ora fra la mattina e il pomeriggio, e a tutte le altre ore
   che possono essere considerate valide sia per un saluto che per un altro?

   Quessto rende l'esercizio difficile e propongo 2 modi per semplificarlo:
   si considera l'ora di inizio _inclusa_ e l'ora di fine _esclusa_,
   es. _buona giornata_ dalle 06:00 a _prima_ delle 12:00.

   L'esercizio è complesso e può avere più soluzioni. Eccone alcune:

   [Soluzione v1](verifica2a/es3_che_ore_sono_v1.flowrun){: .btn }
   [Soluzione v2](verifica2a/es3_che_ore_sono_v2.flowrun){: .btn }
   [Soluzione v3](verifica2a/es3_che_ore_sono_v3.flowrun){: .btn }

   - v1, la più elaborata, ricalcata sul testo dell'esercizio.
   - v2, come v1 ma semplificata di molto, usa le condizioni in cascata.
   - v3, usa un trucco per rendere più facile gestire ore e minuti insieme.
   
   In nessun caso però sono necessari più di 3 o 4 blocchi condizionali (`if`).

## Verifica 2b: algoritmi e diagrammi

Risolvere con [FlowRun](https://www.flowrun.io).

1. Mini calcolatrice (facile)

   Chiedere all'utente 2 numeri, che possono anche essere numeri decimali.
   Chiamiamo questi numeri, ad esempio, `x` e `y`.
   Stampiamo il risultato di tutte le possibili operazioni fra `x` e `y`:

   - `x + y`
   - `x - y`
   - `x * y`
   - `x / y`

   [Soluzione](verifica2b/es1_mini_calcolatrice.flowrun){: .btn }

2. Conta dei nomi (medio)

   Abbiamo 10 utenti.
   Chiedere a ogni utente come si chiama.
   Dopo aver chiesto a tutti, stampare quanti utenti si chiamano _Anna_ e quanti _Marco_.

   Chi sono Anna e Marco?
   - [Anna e Marco](https://it.wikipedia.org/wiki/Anna_e_Marco) su Wikipedia;
   - [Video](https://www.youtube.com/watch?v=r7wvmPM8LYA) su YouTube.

   [Soluzione](verifica2b/es2_conta_nomi.flowrun){: .btn }

3. Calcolatrice (medio)

   Chiedere all'utente 2 numeri, che possono anche essere numeri decimali, e un'operazione da fare.
   Chiamiamo questi numeri, ad esempio, `x` e `y`.
   L'operazione può essere una fra `+`, `-`, `*` e `/`.
   Calcolare e stampare il risultato.

   [Soluzione](verifica2b/es3_calcolatrice.flowrun){: .btn }

4. Morra cinese (molto difficile)

   Due giocatori (giocatore 1 e 2) giocano a sasso-carta-forbici (morra cinese).
   Chiedere ai due giocatori cosa hanno lanciato (se sasso, carta o forbici) e scrivere chi ha vinto.
  
   Regole:
   - carta vince su sasso;
   - forbici vincono su carta;
   - sasso vince su forbici.

   Esempio:
   - i giocatori inseriscono carta e sasso, il programma risponde _vince giocatore 1_
   - i giocatori inseriscono carta e forbici, il programma risponde _vince giocatore 2_
   - i giocatori inseriscono carta e carta, il programma risponde _parità_

   Si ripete il gioco finché qualcuno non vince.

   L'esercizio è complesso e può avere più soluzioni. Eccone alcune:

   [Soluzione v1](verifica2b/es4_morra_cinese_v1.flowrun){: .btn }
   [Soluzione v2](verifica2b/es4_morra_cinese_v2.flowrun){: .btn }
   [Soluzione v3](verifica2b/es4_morra_cinese_v3.flowrun){: .btn }