# crea funzione per aggiungere alla lita elemento
# crea funzione che calcola media

from statistics import mean

letture = []

def aggiungi(id, temp):
    letture.append({"key":id, "value":temp})


def media_temp():
    valori = []
    for l in letture:
        valori.append(l["value"])
        return mean(valori)


# aggiungere misure
aggiungi(1,29)
aggiungi(2,22)
aggiungi(3,36)
aggiungi(4,23)



print(media_temp())