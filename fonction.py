
# Fonction pour calculer age d'une personne

from datetime import date
from datetime import datetime

def age_calcul(date_input = input("Entre votre age : ")):

    date_jour = date.today()
    format = "%d/%m/%Y"             #convert format
    age_recevied_convert = datetime.strptime(date_input, format)
# Verification des conditions
    if date_jour.month > age_recevied_convert.month and date_jour.year > age_recevied_convert.year:
        cal1 = (date_jour.month - age_recevied_convert.month)
        retour1 = (date_jour.year - age_recevied_convert.year)
        print(f"Vous avez {retour1} ans {cal1} mois")
    elif date_jour.month < age_recevied_convert.month :
        cal2 = (age_recevied_convert.month - date_jour.month)
        retour2 = (date_jour.year - age_recevied_convert.year)
        print(f"Vous avez {retour2} ans {cal2} mois")
    elif date_jour.month == age_recevied_convert.month:
        cal3 = (date_jour.month)
        retour3 = (date_jour.year - age_recevied_convert.year)
        print(f"Vous avez {retour3} ans {cal3} mois")
    elif date_jour.year == age_recevied_convert.year:
        cal4 = (date_jour.month - age_recevied_convert.month)
        retour4 = (date_jour.year - age_recevied_convert.year)
        print(f"Vous avez {retour4} ans {cal4} mois1")

    elif date_jour.year < age_recevied_convert.year:
        print("Impossible D'effectuer cette calcul")
        return 0




age_calcul()

