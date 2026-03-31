def time_str(time_ms):
    """
    Funzione che dato un tempo in millisecondi totali (time_ms)
    lo restituisce come stringa, espresso nel formato M:SS.MS
    """
    mm = time_ms // (1000 * 60)
    ss = (time_ms - mm * 1000 * 60) // 1000
    ms = time_ms % 1000
    return f"{mm}:{ss:02d}.{ms:03d}"

# Prove di Formula 1
# ------------------

# Un'auto di Formula 1 fa tre giri di prova all'Autodromo di Monza.
# Chiedere quanti minuti, secondi e millesimi di secondo
# l'auto ha impiegato per concludere ogni giro.
# Calcolare quale è il giro più veloce e stampare il tempo.

# Il calcolo deve essere fatto in millisecondi totali.
# Usare la funzione time_str() per convertire i millisecondi
# totale in un'espressione leggibile.

# Esempio:

# Giro 1, minuti?
# Giro 1, secondi?
# Giro 1, millisecondi?
# Giro 2, minuti?
# ...
# Giro più veloce: ...
# Tempo: ...
