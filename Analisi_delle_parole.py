import re
from collections import defaultdict


def analizza_parole(testo):
    # Converti il testo in minuscolo
    testo = testo.lower()

    # Rimuovi la punteggiatura usando una regex
    testo = re.sub(r' [^\w\s]', '',testo)
    # Dividi il testo in parole
    parole = testo.split()

    # Crea un dzionario per contare le occorrenze delle parole
    conteggio_parole = defaultdict(int)

    # Conta le occorrenze di ciascuna parola
    for parola in parole:
        conteggio_parole[parola] += 1

    # Converti il defaultdict in un dizionario normale
    return dict(conteggio_parole)

# Esempio di utilizzo
testo = "Ciao,ciao! Come stai? Stai bene?"
output = analizza_parole(testo)
print(output)