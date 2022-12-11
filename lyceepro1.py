import lycee
from lycee import *


def exo1():
    figure()
    nb_eoliennes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    nb_parc = [40, 40, 30, 115, 150, 135, 23, 38, 18, 19]
    affiche_tableau([["nb éoliennes"]+nb_eoliennes,["nb parcs"]+nb_parc],markdown=True)
    set_y_min_max(0,160)
    baton(nb_eoliennes, nb_parc, couleur="red",
          titre="constitution des parc éoliens",
          abscisse="nombre d'éoliennes par parc",
          ordonnee="nombre de parcs")
    affiche_graphique()



def exo2():
    """1 créer un programme qui demande et affiche l'âge d'une personne.
       2 après avoir créer une variable mon_age dont la valeur est votre âge,
       modifier le programme pour qu'il retourne la phase suivante si l'utilisateur
       a rentré 35 et que votre ans est 16:
        Vous avez 35 ans, j'ai 15 ans nous avons donc 20 ans de différence.
       3 Si l'utilisateur entre 15 et que vous avez 35 ans : le résultat obtenu sera :
       Vous avez 35 ans, j'ai 15 ans nous avons donc -20 ans de différence.
       Modifier votre programme pour que la différence d'âge soit toujours positive."""

    # question 1
    age = demande("Entrer votre âge")
    # print(f"Vous avez {age} ans")
    # question 2
    mon_age = 57
    difference = mon_age - age
    # question 3
    difference = abs(mon_age - age)
    if mon_age < age:
        difference = age - mon_age
    else:
        difference = mon_age - age
    print(f"Vous avez {age} ans, j'ai {mon_age} ans nous avons donc {difference} ans de différence.")


def exo3():
    # diagramme secteur
    # Source d'énergie et coût de MW électrique
    figure()
    prix_moyen = [90, 50, 80, 140]
    source_energie = ["Gaz", "Nucléaire", "Eolien", "Photovoltaïque"]
    secteur(prix_moyen, source_energie,
            titre="Source d'énergie et coût de MW électrique",
            autopct= lambda prix_moyen: f"{prix_moyen:.2f} €" )
    affiche_graphique()


def exo4():
    # diagramme barre ou colonne
    figure()
    colonne([7, 2, 0, 4], 500, 1000, eff=True, color='orange',
            titre="Puissance parc éolien",
            abscisse="Puissance totale MW",
            ordonnee="nombre de régions")
    affiche_graphique()


def exo5():
    figure(figsize=(6, 6))
    annee = [2012, 2013, 2014, 2015, 2016, 2017, 2018]
    capacite = [7613, 8558, 9285, 10505, 12065, 13757, 15307]
    trace_courbe(annee, capacite, stroke='red', abscisse="Années", ordonnee="Capacité de production (en MW)")
    affiche_graphique()

def exo6():
    figure(1,2)
    colonne([7, 2, 0, 4], 500, 1000, eff=True, color='orange',
            titre="Puissance parc éolien",
            abscisse="Puissance totale MW",
            ordonnee="nombre de régions")
    annee = [2012, 2013, 2014, 2015, 2016, 2017, 2018]
    capacite = [7613, 8558, 9285, 10505, 12065, 13757, 15307]
    trace_courbe(annee, capacite, stroke='red', abscisse="Années", ordonnee="Capacité de production (en MW)")
    affiche_graphique()

def exo7():
    affiche_tableau([["Prénom","âge"],["Paul",15],["Pierre",14],["Jacques",16]]+[["total",45]],mini=10,aligner="gc",markdown=True)

def exo8():
    liste2CSV([[1,2,3,4,5],[11,22,33,44,55]],"essai.txt",affiche=True)
def exo9():
    print(affiche_poly([1, 2, 3], format="python"))
    print(affiche_poly([1, 2, 3]))

def exo10():
    lycee.x=10
    print(demande("entrer votre formule"))

def exo11():
    figure(figsize=(6, 5))
    jour = ["D", "L", "M", "M", "J", "V", "S"]
    stroke("blue")
    jours = [1, 2, 3, 4, 5, 6, 7]
    montreal = [-10, -14, -8, 0, 1, 5, 2]
    toronto = [-7, -10, -2, 3, 5, 4, 0]
    set_y_min_max(-15,10)
    ligne_brisee(jour, montreal, toronto, abscisse="Jour", ordonnee="Température en °C",
                 labels=["Montréal", "Toronto"],
                 marker="v")
    affiche_graphique()

if __name__ == '__main__':
    exo1()
