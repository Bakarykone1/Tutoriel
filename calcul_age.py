
from datetime import date
from datetime import datetime

def age_calcul(date_input):
    """
        :param date_input: date de naissance input par user
        :return:  c'est les differents print qui son retourner a user
    """
    #date_input = input("Quel est votre date de naissance : ")   # if you want tape your birth day by terminal active the code befor
    try:
        date_jour = date.today()
        format_de_date = "%d/%m/%Y"
        birth_date = datetime.strptime(date_input, format_de_date)
        # Vérification des differents condition qui peuvent se posé conditions
        if (birth_date.year < date_jour.year):
            if (birth_date.month < date_jour.month):
                resultat_mois = date_jour.month - birth_date.month
                resultat_annee = date_jour.year - birth_date.year
                return (print(f"votre age est {resultat_annee} ans et {resultat_mois} mois"))
            else:
                resultat_mois = 12 - (birth_date.month - date_jour.month)
                resultat_annee = (date_jour.year - birth_date.year) - 1
                return (print(f"Votre age est {resultat_annee} ans et {resultat_mois} mois"))
        elif (birth_date.year == date_jour.year):
            if (birth_date.month < date_jour.month):
                resultat_mois = date_jour.month - birth_date.month
                resultat_annee = 0
                return (print(f"votre age est {resultat_annee} ans et {resultat_mois} mois"))
            else:
                resultat_annee = 0
                resultat_mois = 12 - (birth_date.month - date_jour.month)
                return (print(f"Votre age est {resultat_annee} ans et {resultat_mois} mois"))
        else:
            return (print(f"Impossible votre année de naissance n'est pas correct {birth_date.year} est superieur que {date_jour.year}, veuillez reprendre s'il vous plait "))
    except ValueError :
        return (print("le format de date incorrect, veuillez reprendre. Exemple : jour/mois/annee"))


#age_calcul()
age_calcul("")
