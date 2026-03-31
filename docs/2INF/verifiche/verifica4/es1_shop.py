def netto(totale):
    """Calcola il netto a partire dal totale compreso di IVA"""
    return round(100 / (100 + 22) * totale, 2)

def iva(totale):
    """Calcola l'IVA scorporandola dal totale compreso di IVA"""
    return round(totale - netto(totale), 2)

# Ordine di un negozio online
# ---------------------------

# Chiediamo quanti acquisti ha fatto.
# Per ogni acquisto, chiediamo il nome dell'oggetto,
# la quantità e il prezzo del singolo oggetto.

# Stampiamo alla fine quanto è il totale dell'ordine, IVA inclusa.

# Stampiamo poi il prezzo netto e l'IVA dell'ordine,
# utilizzando le funzioni netto() e iva() definite sopra.

n = int(input("Quanti acquisti?"))

total = 0

for i in range(n):
    name = input("Nome?")
    quantity = int(input("Quantità?"))
    price = float(input("Prezzo?"))

    total = total + quantity * price

print("Totale:", round(total, 2))
print("Netto:", netto(total))
print("IVA:", iva(total))