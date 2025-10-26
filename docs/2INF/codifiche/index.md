---
title: Codifiche
parent: 2INF
layout: page
nav_order: 3
---

# Codifiche

Vediamo ora come è possibile codificare le informazioni
come testi, immagini, audio e video tramite _byte_.

Convenzionalmente, i _byte_ sono rappresentati sotto forma [esadecimale](../esadecimale/index.md).

1. TOC
{: toc }

## Bit

Si chiama [_bit_](https://it.wikipedia.org/wiki/Bit) qualcosa che può assumere solo valori `0` e `1`,
oppure `True` o `False`, o altri valori che hanno significato caso per caso,
ad esempio `presente` o `assente` in un appello a scuola, 
`acceso` o `spento` nel caso di una luce o di un dispositivo,
`bianco` o `nero` in una scacchiera, `presenza di segnale` o
`assenza di segnale` in un circuito elettronico, `testa` o `croce` nel lancio
di una moneta e molto altro.

Un valore _booleano_ può quindi essere rappresentato con un _bit_.

## Byte

Un [_byte_](https://it.wikipedia.org/wiki/Byte) è formato da 8 _bit_
ed è l'unità di misura fondamentale dell'informazione.

Calcolando tutte le possibili combinazioni di _zero_ e _uno_,
abbiamo visto che un _byte_ può contenere 256 possibili valori che,
convenzionalmente, rappresentano i numeri da **0** a **255** in decimale.
Tutti i possibili valori di un _byte_ possono anche essere rappresentati
in esadecimale, con i numeri a due cifre
[esadecimali](../esadecimale/index.md#contare-in-esadecimale) da **00** a **FF**.

Oltre ai numero interi, è possibile rappresentare altro.

Vedremo che con un solo _byte_ è possibile rappresentare una lettera
dell'alfabeto latino, cioè l'alfabeto in comune alle lingue europee,
ad esempio `A`-`Z` ma anche minuscole `a`-`z` e altri simboli `!?+*` ...

Un _byte_ da solo non è sufficiente a fare molto. Si utilizzano spesso
molti più _byte_ messi insieme a formare quantità di informazioni sempre più grandi.

## KB, MB, GB e altre unità di misura

Si definiscono quindi le unità di misura nel
[Sistema Internazionale](https://it.wikipedia.org/wiki/Prefissi_del_Sistema_internazionale_di_unit%C3%A0_di_misura):

- **KB** (kilobyte) = 1.000 byte
- **MB** (megabyte) = 1.000 KB = 1.000.000 byte
- **GB** (gigabyte) = 1.000 MB = 1.000.000 KB = 1.000.000.000 byte
- **TB** (terabyte) = 1.000 GB = ...

Per motivi tecnici, essendo tutta l'informatica basata sulle potenze del 2,
esistono e vengono in realtà usate più spesso delle unità del Sistema Internazionale
riportate sopra anche le seguenti unità definite tramite i
[prefissi binari](https://it.wikipedia.org/wiki/Prefissi_per_multipli_binari):

- **KiB** (kibibyte) = 1.024 byte
- **MiB** (mebibyte) = 1.024 KiB = 1024² byte
- **GiB** (gibibyte) = 1.024 MiB = 1024³ byte
- **TiB** (tebibyte) = 1.024 GiB = ...

1.024 è una potenza del 2, cioè 2¹⁰, ed è una cifra _più tonda_ di 1.000
per un computer, mentre 1.000 è una cifra _più tonda_ per un umano.

Nella pratica, nessuno pronuncia mai _kibibyte_ o _mebibyte_ ma sempre _kilobyte_ e _megabyte_
intedendo a volte i multipli di 1.000 a volte i multipli di 1.024, facendo
una _gran confusione_. Se non specificato altrimenti, cioè se non si legge _KiB_ o _MiB_,
bisogna tentare di capire dal contesto quale delle due si intenda.

Sì, si fa una _gran confusione_.

## Codifica di testo ASCII
_(in via di pubblicazione)_

## Codifica di testo Unicode
_(in via di pubblicazione)_

## Codifica di una immagine
_(in via di pubblicazione)_

## Codifica di un audio
_(in via di pubblicazione)_

## Codifica di un video
_(in via di pubblicazione)_