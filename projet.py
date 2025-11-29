import json


FICHIER_SAUVEGARDE = "classe.json"

def charger_classe():
    """Charge la classe depuis le fichier JSON"""
    try:
        with open(FICHIER_SAUVEGARDE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, IOError):
        print("Fichier non trouvé ou erreur de chargement, utilisation des données par défaut.")
    
    
    return [
        ["Alice", 20, 15.5],
        ["Bob", 19, 12.0],
        ["Charlie", 22, 16.0]
    ]

def sauvegarder_classe(classe):
    """Sauvegarde la classe dans un fichier JSON"""
    try:
        with open(FICHIER_SAUVEGARDE, 'w', encoding='utf-8') as f:
            json.dump(classe, f, ensure_ascii=False, indent=2)
        print("✓ Données sauvegardées.")
    except IOError:
        print("Erreur lors de la sauvegarde.")

def afficher_classe_format_tableau(classe):
    """Affiche la classe en format tableau"""
    if not classe:
        print("La classe est vide.")
        return
    
    
    print("LISTE DES ÉTUDIANTS")
    
    print(f"{'No':<3} {'Nom':<15} {'Âge':<5} {'Note':<6}")
    
    
    for index, (nom, age, note) in enumerate(classe, start=1):
        print(f"{index:<3} {nom:<15} {age:<5} {note:<6.1f}")
    print(f"\nTotal : {len(classe)} étudiant(s)")

def afficher_classe(classe):
    """Affiche tous les étudiants de la classe"""
    if not classe:
        print("La classe est vide.")
        return
    for index, (nom, age, note) in enumerate(classe, start=1):
        print(f"{index}. {nom} — {age} ans — note {note}")

def ajouter_etudiant(classe):
    nom = input("Nom : ").strip()
    try:
        age = int(input("Âge : "))
        note = float(input("Note : "))
    except ValueError:
        print("Saisie invalide.")
        return
    classe.append([nom, age, note])
    print(f"{nom} ajouté.")

def confirmer_suppression(etudiant):
    """Demande confirmation avant suppression"""
    print(f"\nVous allez supprimer : {etudiant[0]} — {etudiant[1]} ans — note {etudiant[2]}")
    confirmation = input("Confirmer la suppression (o/n) ? ").strip().lower()
    return confirmation in ['o', 'oui', 'y', 'yes']

def supprimer_etudiant(classe):
    if not classe:
        print("Rien à supprimer.")
        return
    try:
        index = int(input("Numéro de l'étudiant à supprimer : ")) - 1
        etudiant = classe[index]
        
        if confirmer_suppression(etudiant):
            etudiant_supprime = classe.pop(index)
            print(f"{etudiant_supprime[0]} supprimé.")
        else:
            print("Suppression annulée.")
            
    except (ValueError, IndexError):
        print("Index invalide.")

def mettre_a_jour_etudiant(classe):
    if not classe:
        print("Classe vide.")
        return
    try:
        index = int(input("Numéro de l'étudiant à modifier : ")) - 1
        etudiant = classe[index]
    except (ValueError, IndexError):
        print("Index invalide.")
        return

    print(f"Modification de {etudiant[0]} (laisser vide pour ne pas changer).")
    nouveau_nom = input("Nouveau nom : ").strip()
    if nouveau_nom:
        etudiant[0] = nouveau_nom

    entree_age = input("Nouvel âge : ").strip()
    if entree_age:
        try:
            etudiant[1] = int(entree_age)
        except ValueError:
            print("Âge ignoré (saisie invalide).")

    entree_note = input("Nouvelle note : ").strip()
    if entree_note:
        try:
            etudiant[2] = float(entree_note)
        except ValueError:
            print("Note ignorée (saisie invalide).")

def afficher_statistiques(classe):
    if not classe:
        print("Pas de données.")
        return
    notes = [etudiant[2] for etudiant in classe]
    moyenne = sum(notes) / len(notes)
    meilleure = max(classe, key=lambda e: e[2])
    pire = min(classe, key=lambda e: e[2])
    print(f"Moyenne des notes : {moyenne:.2f}")
    print(f"Meilleure note : {meilleure[2]} ( {meilleure[0]} )")
    print(f"Moins bonne note : {pire[2]} ( {pire[0]} )")

def rechercher_etudiant(classe):
    """Recherche un étudiant par nom"""
    if not classe:
        print("La classe est vide.")
        return
    
    nom_recherche = input("Nom à rechercher : ").strip().lower()
    if not nom_recherche:
        print("Veuillez entrer un nom.")
        return
    
    resultats = []
    for index, etudiant in enumerate(classe):
        if nom_recherche in etudiant[0].lower():
            resultats.append((index, etudiant))
    
    if resultats:
        print(f"\n{len(resultats)} résultat(s) trouvé(s) :")
        for index, etudiant in resultats:
            print(f"{index + 1}. {etudiant[0]} — {etudiant[1]} ans — note {etudiant[2]}")
    else:
        print("Aucun étudiant trouvé.")


classe = charger_classe()
print(" Données chargées depuis le fichier.")

while True:
    print("\nGestion de la classe")
    print("1. Afficher tous les étudiants")
    print("2. Afficher en tableau formaté")
    print("3. Ajouter un étudiant")
    print("4. Supprimer un étudiant")
    print("5. Modifier un étudiant")
    print("6. Statistiques")
    print("7. Rechercher un étudiant")
    print("s. Sauvegarder")
    print("q. Quitter")

    choix = input("Choix : ").strip().lower()

    if choix == "1":
        afficher_classe(classe)
    elif choix == "2":
        afficher_classe_format_tableau(classe)
    elif choix == "3":
        ajouter_etudiant(classe)
        sauvegarder_classe(classe)
    elif choix == "4":
        supprimer_etudiant(classe)
        sauvegarder_classe(classe)
    elif choix == "5":
        mettre_a_jour_etudiant(classe)
        sauvegarder_classe(classe)
    elif choix == "6":
        afficher_statistiques(classe)
    elif choix == "7":
        rechercher_etudiant(classe)
    elif choix == "s":
        sauvegarder_classe(classe)
    elif choix == "q":
        sauvegarder_classe(classe)
        print("Au revoir.")
        break
    else:
        print("Option inconnue.")


