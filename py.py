"""def welcome():
    print("Bienvenu")
    nb1 = int(input("Entrer le premier nombre "))
    nb2 = int(input("Entrer le deuxieme nombre "))
    resultat = nb1 + nb2
    print(f"Le resultat est : {resultat}")


welcome()"""

"""
def password():
    max_essais = 3

    for essai in range(max_essais):
        username = input("Entrer le nom d'utilisateur : \n")
        password = input("Entrer le mot de passe : \n")

        if username == "admin" and password == "Admin123":
            print("\n\t✅ Vous êtes connecté !!")
            return  # Quitte la fonction dès la connexion réussie

        restants = max_essais - (essai + 1)
        if restants > 0:
            print(f"\n\t❌ Nom d'utilisateur ou mot de passe incorrect.")
            print(f"\t   Il vous reste {restants} essai(s).\n")

    print("\n\t🔒 Compte bloqué : nombre maximum de tentatives atteint.")


password()
"""
