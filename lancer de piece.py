from lycee import *
from random import randint
def sac_de_pieces(nbre_piece, **kwargs)->list[float]:
    """Retourne la fréquence de Pile pour 200 lancés
    le pourcentage de pièces sans défaut est de 99.
    On peut le modifier avec le paramètre optionnel pourcentage
    ex: poucentage=85"""
    pourcentage=kwargs.get("pourcentage",99)
    pieces_bonnes = nbre_piece*pourcentage//100
    pieces_mauvaise = nbre_piece - pieces_bonnes
    sac = []
    for i in range(pieces_bonnes):
        somme = 0
        for i in range(200):
            somme += randint(0, 1)
        sac.append(somme/200)

    for i in range(pieces_mauvaise):
        somme = 0
        for i in range(100):
            somme += randint(0, 1)
        sac.append(somme / 100)
    return sac

sac=sac_de_pieces(40)
sac1=sac_de_pieces(40, pourcentage=85)
xi=[i for i in range(1,41)]
figure()
nuage(xi,sac,sac1,c="b",marker="+",abscisse="Numero de la pièce",ordonnee="Fréquence de Pile",titre="Fréquence de pile pour 40 pièces avec 200 lancés",labels=["Sac1","Sac2"])
ligne(0,0.43,40,0.43,linestyle="--",c="r")
ligne(0,0.57,40,0.57,linestyle="--",c="r")
affiche_graphique()