from lycee import *


def tirage_avec_remise(nbre_de_tirages: int) -> float:
    c = 0
    for i in range(nbre_de_tirages):
        b = sac_de_boule(["bleu", "verte", "rouge", "violette", "orange"])
        if b == "verte":
            c = c + 1
    f = c / nbre_de_tirages
    print(f)


# for t in range(4):
#     tirage_avec_remise(10000)


def lance_de(nb_lance):
    tirages = []
    c = 0
    for i in range(nb_lance):
        if lance_de_de() == 5:
            c = c + 1
        tirages.append(c / (i + 1))
    return tirages


# figure()
# xi = [i + 1 for i in range(1000)]
# freq = lance_de(1000)
# erreur = [1 / 6 - freq[i] for i in range(1000)]
# trace_courbe(xi, freq, erreur, labels=["fréquence", "erreur"])
# affiche_graphique()

def tirage_bonbon(nb_tirages):
    c = 0
    for i in range(nb_tirages):
        b = sac_de_boule(["menthe", "menthe", "menthe","menthe", "menthe", "menthe","menthe", "cassis", "cassis","cassis"])
        if b == "menthe":
            c = c + 1
    f = c / nb_tirages
    print(f)

tirage_bonbon(1000)