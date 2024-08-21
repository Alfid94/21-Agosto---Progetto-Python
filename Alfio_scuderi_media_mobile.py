# Definisci la funzione per calcolare la media mobile
def medie_mobile (numeri, n):
    # Lista che conterrà le medie mobili calcolate
    medie_mobili = []

    # Scorri la lista dei numeri
    for i in range(len(numeri)):
    # Seleziona gli ultimi n elementi (o meno, se siamo all'inizio della lista)
        if i < n - 1:
            finestra = numeri[:i+1]
        else:
            finestra = numeri[i-n+1:i+1]

    # Calcola la media della finestra
    media = sum(finestra) / len(finestra)
    medie_mobili.append(media)

    return medie_mobili

# Esempio di utilizzo
if __name__ == "__main__":
  numeri = [1,54,3,65,5,6,7,8,76,10]
  n = 3
  risultato = medie_mobile(numeri, n)
print("la media mobile è", risultato)
