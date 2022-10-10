from datetime import datetime

def calcul_age (date_get=" / / "):

    reference_jour = 365
    date = datetime.today()
    date_get = date_get
    try:
        resultat = ((date - date_get) / reference_jour)
    except:
        print("impossible d'effectuer cette operation")
    else :
        print(f"votre age est de {resultat} ans")


calcul_age(12/2/2001)

