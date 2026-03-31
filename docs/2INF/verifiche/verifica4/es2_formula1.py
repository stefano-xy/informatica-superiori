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

fastest_lap = None
fastest_ms = None

for lap in range(1, 4):
    mm = int(input(f"Giro {lap}, minuti:"))
    ss = int(input(f"Giro {lap}, secondi:"))
    ms = int(input(f"Giro {lap}, millisecondi:"))

    lap_ms = mm * 1000 * 60 + ss * 1000 + ms

    print(f"Giro {lap}: {time_str(lap_ms)}")
    
    if fastest_ms is None or lap_ms < fastest_ms:
        fastest_lap = lap
        fastest_ms = lap_ms

print(f"Giro più veloce: {fastest_lap}")
print(f"Tempo: {time_str(fastest_ms)}")