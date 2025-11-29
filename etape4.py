classe = [
    ["Alice", 20, 15.5],
    ["Eve", 19, 14.0],
    ["Charlie", 21, 16.5]
]
classe.append(["Diana", 22, 13.0])
print(classe)

for index, (nom, age, note) in enumerate(classe, start=1):
    print(f"Étudiant {index} : {nom} ({age} ans) – note {note}")



classe_dict = [
    {"nom": "Alice", "age": 20, "note": 15.5},
    {"nom": "Eve", "age": 19, "note": 14.0},
    {"nom": "Charlie", "age": 21, "note": 16.5}
]
classe_dict.append({"nom": "Diana", "age": 22, "note": 13.0})

age_charlie = classe[2][1]
print(age_charlie)  # 21

classe[2][2] = 17.0  # met à jour la note de Charlie