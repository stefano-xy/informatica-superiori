---
title: Esadecimale
parent: 2INF
layout: page
nav_order: 2
---

# Sistema di numerazione esadecimale

Il [sistema esadecimale](https://it.wikipedia.org/wiki/Sistema_numerico_esadecimale),
_hexadecimal_ in inglese, spesso abbreviato _hex_, cioè a base 16,
viene usato in informatica probabilmente anche più del binario.
Ha tanti vantaggi fra cui quello di essere _comodo_, che non è da sottovalutare.

Ogni numero in esadecimale è formato da cifre che possono avere 16 valori.
Per rappresentare i valori da _zero_ a _nove_ usiamo le cifre classiche, **0** ... **9**.

Per rappresentare i valori da _dieci_ a _quindici_ usiamo le prime 6 lettere dell'alfabeto:

- **A** = 10
- **B** = 11
- **C** = 12
- **D** = 13
- **E** = 14
- **F** = 15

Usare le maiuscole o le minuscole è indifferente. In questo corso useremo sempre le maiuscole
ma su internet possiamo trovare facilmente numeri o codici esadecimali che usano le minuscole.

1. TOC
{: toc }

## Contare in esadecimale

Siamo in un sistema di numerazione in cui dopo il **9** viene **A** e
una volta raggiunto **F** torniamo a **0** con riporto di 1.

Contiamo ad esempio i primi 20 numeri, partendo da 0:

0, 1, 2, 3, 4, 5, 6, 7,
8, 9, **A**, **B**, **C**, **D**, **E**, **F**,
10, 11, 12, 13 ...

Continuiamo:

... 14, 15, 16, 17, 18, 19, **1A**, 1B,
1C, 1D, 1E, 1F, 20, 21, 22, 23, 24 ...

Notiamo come dopo il **9** venga **A** e solo dopo **F** venga **0**.

... 58, 59, **5A**, 5B, 5C, 5D, 5E, 5F, **60**, 61, 62 ...

Anche la prima cifra, arrivata a **9**, va incrementata con **A**:

... 99, 9A, 9B, 9C, 9D, 9E, 9F, **A0**, A1, A2, A3,
A4, A5, A6, A7, A8, A9, **AA**, AB, AC,
AD, AE, AF, **B0**, B1, B2, B3 ...

Per finire, arrivati a **FF** passiamo a **100**:

... FB, FC, FD, FE, FF, **100**, 101, 102, ...

I primi 256 numeri si scrivono da **0** (0) a **FF** (255).

{: .highlight }
**256** in informatica è una cifra _molto tonda_, in quanto
è una potenza del 2, per la precisione 2^8, e anche 8 stesso
è una potenza del 2. In quanto un [byte](../codifiche/index.md#byte)
contiene 8 bit, con i numeri esadecimali da **00** a **FF**
si possono scrivere facilmente tutti i possibili valore
che un _byte_ può avere.

Dividendo il _byte_ in 2 metà, una con i 4 _bit_ più alti
e l'altra con i 4 _bit_ più bassi, la prima cifra esadecimale
indica il valore dei _bit_ alti, la seconda cifra
il valode dei _bit_ bassi.

_Più comodo di così?_ 😊

## Da esadecimale a decimale

Così come per i numeri [decimali](../binario/index.md#numeri-decimali) e
[binari](../binario/index.md#da-binario-a-decimale), possiamo scomporre un
numero esadecimale in potenze del 16 e convertirlo in decimale,
ricordandosi sempre il valore decimale corrispondente alle lettere da **A** a **F**.

Esempio:

```math
0xA5E = 10 * 16^2 + 5 * 16^1 + 14 * 16^0
  321
```

Abbiamo indicato per chiarezza le posizioni, che corrispondono agli
esponenti delle potenze del 16, e il prefisso `0x` convenzionalmente usato
per indicare un numero esadecimale e non confonderlo con un numero
di un altro sistema di numerazione. Abbiamo usato `0b` per i binari.
Il prefisso non ha alcun effetto nei calcoli e va ignorato.

Notiamo anche che **A** è stato scritto come **10**
mentre **E** è stato scritto come **14** in decimale.

Completiamo il calcolo:

```math
0xA5E = 10 * 256 + 5 * 16 + 14 = 2560 + 80 + 14 = 2654
```

Il numero esadecimale **A5E** corrisponde al decimale **2654**.

I calcoli sono più complessi che per il binario, ma il procedimento è lo stesso.

Altri esempi:

```math
0x8C0 = 8 * 16^2 + 12 * 16
      = 8 * 256  + 12 * 16 = 2048 + 192 = 2240

0x9AA3 = 9 * 16^3 + 10 * 16^2 + 10 * 16^1 + 3 * 16^0
       = 9 * 4096 + 10 * 256  + 10 * 16   + 3 = 36864 + 2560 + 160 + 3 = 39587

0xC007A = 12 * 16^4  + 7 * 16^1 + 10 * 16^0
        = 12 * 65536 + 7 * 16   + 10 = 786432 + 112 + 10 = 786554
```

Bastano poche cifre esadecimali per creare numeri decimali molto grandi.

Alcuni numeri speciali:

```math
  0x0 = 0
  0x4 = 4
  0x8 = 8
  0xC = 12
 0x10 = 16
 0x40 = 64
 0x80 = 128
 0xC0 = 192
0x100 = 256
```

Notate che in esadecimale **80** (128) è la metà di **100** (256) così come
**8** è la metà di **10** (16). Sembra strano ma non lo è, se si considera
che dopo l'8 vengono altre 8 cifre e non 2 prima di arrivare a 10.

## Da decimale a esadecimale
_(in via di pubblicazione)_

## Esadecimale sul web
_(in via di pubblicazione)_
