---
title: Binario
parent: 2INF
layout: page
nav_order: 1
---

# Sistema di numerazione binario

Così come i numeri decimali sono composti da 10 cifre, da _zero_ a _nove_,
esistono altri sistemi di numerazione che operano con meno o più cifre.

Il [sistema binario](https://it.wikipedia.org/wiki/Sistema_numerico_binario)
opera soltanto con le cifre _zero_ e _uno_.

_A cosa serve? Perché?_

La rappresentazione binaria è importante in quanto il mondo moderno, di internet,
delle telecomunicazioni, dell'informatica è costruito sull'elettronica digitale.
L'elettronica digitale processa segnali chiari e nitidi, cioè segnali
che possono essere _presenti_ o _assenti_ in un circuito elettronico e non,
per esempio, _presenti a metà_ o _presenti un po'_ o _presenti all'84%_.

Nell'elettronica digitale tutto è _bianco_ o _nero_, tutto è _acceso_
o _spento_, tutto è _zero_ o _uno_ e non _0 virgola 71_ oppure _1 virgola 183_.
È [combinando](../codifiche/index.md) questi _zero_ e _uno_ in vari modi che si rappresenta
l'informazione, ad esempio il contenuto di un file di testo, una foto,
un vocale su WhatsApp, un video su YouTube, un software stesso.

{: .highlight }
Poiché memorie, processori, segnali elettrici operano in digitale,
_zero_ e _uno_ possono essere memorizzati _facilmente_ su un supporto
come un disco, una memoria, oppure trasmessi su internet via cavo o WiFi,
cosa che non si può dire altrettanto di 0,71 e 1,183.

È quindi importante sapere come operare con i numeri binari
perché questo è alla base del mondo moderno.

1. TOC
{: toc }

## Numeri decimali

Per il numero decimale **9468**, se contiamo da destra verso sinistra
le posizioni delle cifre, partendo da zero, notiamo che:

- il **9** è in posizione 3
- il **4** è in posizione 2
- il **6** è in posizione 1
- l'**8** è in posizione 0

Possiamo scomporre il 9468 in potenze del 10, dove ogni potenza
ha come esponente la posizione della cifra che moltiplica:

```math
9468 = 9 * 10^3 + 4 * 10^2 + 6 * 10^1 + 8 * 10^0
3210
```

Abbiamo indicato sotto ogni cifra la sua posizione, per chiarezza.

Riscriviamo:

```math
9468 = 9 * 1000 + 4 * 100 + 6 * 10 + 8
```

Se si fa tutto il calcolo, si scopre che il risultato è, come previsto, **9468**.

Questa vale per i numeri decimali ma lo stesso procedimento
può essere applicato per i numeri **binari** e [esadecimali](../esadecimale/index.md#da-esadecimale-a-decimale).

## Da binario a decimale

È più facile mostrare come convertire un numero binario in decimale
che viceversa, quindi cominciamo da qui.

Ipotizziamo di avere il numero binario **101101**. Questo può essere
descritto con le potenze del 2 invece che del 10, dove ogni cifra
è moltiplicata per 2 elevato alla sua posizione:

```math
0b101101 = 1 * 2^5 + 0 * 2^4 + 1 * 2^3 + 1 * 2^2 + 0 * 2^1 + 1 * 2^0
  543210
```

Anche in questo caso abbiamo indicato sotto ogni cifra la sua posizione, per chiarezza.

Il prefisso `0b` serve per indicare che il numero è binario, e non confonderlo
con un numero decimale. Per i numeri [esadecimali](../esadecimale/index.md)
utilizziamo invece il prefisso prefisso `0x`. Senza prefisso intendiamo numeri decimali.
Il prefisso non ha alcun effetto nei calcoli e va ignorato.

Eliminiamo le moltiplicazioni `1*` in quanto superflue e
gli addendi che iniziano con `0*` in quanto il loro valore è sempre zero:

```math
0b101101 = 2^5 + 2^3 + 2^2 + 2^0
  543210
```

Rimangono sono le potenze del 2 che corrispondono agli _uno_. Ogni potenza
ha l'esponente che corrisponde alla sua posizione.

Completiamo il calcolo:

```math
0b101101 = 32 + 8 + 4 + 1 = 45
```

A **101101** in binario corrisponde **45** in decimale.

Altri esempi di conversioni da binario e decimale:

```math
0b1011 = 2^3 + 2^1 + 2^0 = 8 + 2 + 1 = 11
0b11001 = 2^4 + 2^3 + 2^0 = 16 + 8 + 1 = 25
0b101110 = 2^5 + 2^3 + 2^2 + 2^1 = 32 + 8 + 4 + 2 = 46
```

## Da decimale a binario
_(in via di pubblicazione)_

## Somma fra numeri binari
_(in via di pubblicazione)_

## Operazioni `AND`, `OR`, `NOT` bit per bit
_(in via di pubblicazione)_