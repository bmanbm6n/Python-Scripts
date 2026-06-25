#CFA en Eur/Doll
CFA = input("\t \nEntrez le CFA a convertir : ")
EURO = 655.96
DOLLARS = 596.04
Cfa_en_Euro = int(CFA)/EURO
Cfa_en_Dollars = int(CFA)/DOLLARS
Diff_Eur_Doll = Cfa_en_Euro - Cfa_en_Dollars
print("\t\n - " + CFA + " Euro est égal a : " + str(Cfa_en_Euro))
print("\t\n - " + CFA + " Dollars est égal à " + str(Cfa_en_Dollars) + " \n")
print("La difference entre " + str(EURO) + " EURO et " + str(DOLLARS) + " est de " + str(Diff_Eur_Doll) + "\t \n")