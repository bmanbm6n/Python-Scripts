#Eur/Doll en CFA

CFA = input("\t \nEntrez le nombre a convertir : ")
EURO = 655.96
DOLLARS = 596.04
Euro_en_Cfa = EURO*int(CFA)
Dollars_en_Cfa = DOLLARS*int(CFA)
Diff_Eur_Doll = Euro_en_Cfa - Dollars_en_Cfa
print("\t\n - " + CFA + " Euro est égal a : " + str(Euro_en_Cfa))
print("\t\n - " + CFA + " Dollars est égal à " + str(Dollars_en_Cfa) + " \n")
print("La difference entre " + str(EURO) + " EURO et " + str(DOLLARS) + " est de " + str(Diff_Eur_Doll) + "\t \n")