from ClassDate import Date


def SaisieDate():
    while True:
        jour = input('    Jour : ')
        mois = input('    Mois : ')
        annee = input('    Année : ')
        try:
            date = Date(int(jour), int(mois), int(annee))
            return date
            break
        except IndexError:
            print("        Cette date n'existe pas.")
        except ValueError:
            print("        L'année doit être comprise entre 1000 et 9999.")
        except:
            print("        Vous devez saisir des nombres entiers.")



# Saisie et affichage de la date de naissance
print("Saisissez votre date de naissance :")
d1 = SaisieDate()
print("\nVotre date de naissance est le", d1)

print("\nSaisissez la date à laquelle vous souhaitez connaître votre âge :")
d2 = SaisieDate()
print("Le", d2, ", votre âge est de", (d2 - d1)[0], "ans et", (d2 - d1)[1], "jours (à un jour près).")

