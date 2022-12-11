def conversion_longueur1(valeur: str, unite: str):
    unites = {"km": 3, "hm": 2, "dam": 1, "m": 0, "dm": -1, "cm": -2, "mm": -3}
    v, u = valeur.split()
    v = v.split(".")
    decalage = (unites[u] - unites[unite])
    if len(v)==2:
        d = str(int(v[1]))
        decalage-=len(d)
        v=v[0]+d
    else:
        v=v[0]
    if decalage > 0:
        return int(v + "0" * decalage)
    else:
        if -decalage < len(v):
            partie_entiere = int(v[:decalage])
            partie_decimale = int(v[decalage:])
            if partie_decimale == 0:
                return partie_entiere
            else:
                return float(f"{partie_entiere}.{partie_decimale}")
        else:
            return float("0." + "0" * (-decalage - len(v)) + v)

def conversion_longueur(valeur:str, unite:str):
    unites = {"km":3, "hm":2, "dam":1, "m":0, "dm":-1, "cm":-2, "mm":-3}
    v, u = valeur.split()
    decalage = unites[u]-unites[unite]
    return round(float(v)*10**decalage,abs(decalage))

print(conversion_longueur("0.12 km", "m"))