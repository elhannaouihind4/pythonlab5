classe = [
    ["Alice", 20, 15.5],
    ["Eve", 19, 14.0],
    ["Charlie", 21, 16.5],
    ["Diana", 22, 13.0]
]


classe.sort(key=lambda ligne: ligne[2], reverse=True)
print("Tri par note décroissante:")
for etudiant in classe:
    print(f"  {etudiant[0]}: {etudiant[2]}")


notes = [etudiant[2] for etudiant in classe]
moyenne = sum(notes) / len(notes)
print(f"\nMoyenne de la classe: {moyenne:.2f}")

note_max = max(notes)
note_min = min(notes)
print(f"Note maximale: {note_max}")
print(f"Note minimale: {note_min}")


def rechercher_etudiant(nom):
    for etudiant in classe:
        if etudiant[0].lower() == nom.lower():
            return etudiant
    return None


def rechercher_avec_next(nom):
    return next((etudiant for etudiant in classe 
                if etudiant[0].lower() == nom.lower()), None)


nom_recherche = input("\nEntrez un nom à rechercher: ")
resultat = rechercher_avec_next(nom_recherche)

if resultat:
    print(f"Trouvé: {resultat[0]}, {resultat[1]} ans, note: {resultat[2]}")
else:
    print("Étudiant non trouvé")


notes_seuil = 15.0
etudiants_notes_elevees = [etudiant for etudiant in classe if etudiant[2] >= notes_seuil]
print(f"\nÉtudiants avec note >= {notes_seuil}:")
for etudiant in etudiants_notes_elevees:
    print(f"  {etudiant[0]}: {etudiant[2]}")


import copy



print("Copie superficielle vs profonde")


classe_copie_superficielle = classe[:]  
print("Avant modification:")
print(f"Original: {classe[0]}")
print(f"Copie: {classe_copie_superficielle[0]}")


classe_copie_superficielle[0][1] = 99  

print("\nAprès modification de la copie superficielle:")
print(f"Original: {classe[0]}")  
print(f"Copie: {classe_copie_superficielle[0]}")
print(" L'original est modifié car les sous-listes sont partagées")


classe_copie_profonde = copy.deepcopy(classe)
classe_copie_profonde[0][1] = 100  

print("\nAvec copie profonde:")
print(f"Original: {classe[0]}")  
print(f"Copie: {classe_copie_profonde[0]}")
print(" L'original reste intact")




classe_dict = [
    {"nom": etudiant[0], "age": etudiant[1], "note": etudiant[2]}
    for etudiant in classe
]


print("Conversion en dictionnaires")



for etudiant in classe_dict:
    print(f"{etudiant['nom']}: {etudiant['age']} ans, note {etudiant['note']}")


nom = "Alice"
etudiant_trouve = next((e for e in classe_dict if e["nom"] == nom), None)
if etudiant_trouve:
    print(f"\n{etudiant_trouve['nom']} a {etudiant_trouve['age']} ans")