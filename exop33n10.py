"""Fin août 2020, les medias annonçaient une probable stabilisation des prix des boites
de masques chirurgicaux avec une baisse d'au moins 30% du prix par rapport à mai 2020
Problématique :
L'annoce des médias c'est-elle vérifié en septembre 2020?

1 le tableau ci-dessous rassemble les prix des boites de 50 masques relevés en septembre 2020
p =[9.90, 14.90,25.00,12.90,11.50,
15.00,24.00,38.90,24.90,29.90,
24.90,18.50,14.50,14.90,24.90]

déterminer en créant les fonctions appropriée qui renvoie une valeur approchée avec 2 chiffres après la virgule:
  mode (conseil trier le tableau avec la fonction sort()
  moyenne
  médiane
  étendue
  ecart interquartile
  ecart type
  """
import math


def mode(elements: list[float]) -> float:
    """retourne la valeur la plus fréquente"""
    elements.sort()
    nbre_element = len(elements)
    valeur_la_plus_frequente = elements[0]
    valeur = elements[0]
    nbre = 1
    nbre_maxi = 1
    for i in range(1, nbre_element):
        if elements[i] == valeur:
            nbre += 1
        else:
            if nbre > nbre_maxi:
                nbre_maxi = nbre
                valeur_la_plus_frequente = valeur
            valeur = elements[i]
            nbre = 1
    return valeur_la_plus_frequente


def moyenne(elements: list[float]) -> float:
    somme = 0
    nbre_element = len(elements)
    for e in elements:
        somme += e
    return round(somme / nbre_element, 2)


def mediane(elements: list[float]) -> float:
    elements.sort()
    nbre_element = len(elements)
    if nbre_element % 2 == 1:
        return elements[nbre_element // 2]
    else:
        return (elements[nbre_element // 2] + elements[(nbre_element // 2) - 1]) / 2


def etendue(elements: list[float]) -> float:
    elements.sort()
    return elements[-1] - elements[0]


def interquartille(elements: list[float]) -> float:
    elements.sort()
    nbre_element = len(elements)
    q1 = elements[(nbre_element // 4)]
    q3 = elements[(nbre_element * 3 // 4)]
    return round(q3 - q1, 2)


def ecart_type(elements: list[float]) -> float:
    m = moyenne(elements)
    nbre_element = len(elements)
    somme = 0
    for e in elements:
        somme += (e - m) ** 2
    return round(math.sqrt(somme / nbre_element), 2)


if __name__ == '__main__':
    p = [9.90, 14.90, 25.00, 12.90, 11.50,
         15.00, 24.00, 38.90, 24.90, 29.90,
         24.90, 18.50, 14.50, 14.90, 24.90]

    print(mode(p))
    print(moyenne(p))
    print(mediane(p))
    print(etendue(p))
    print(interquartille(p))
    print(ecart_type(p))
