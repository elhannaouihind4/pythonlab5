etudiants = ["Alice", "Bob", "Charlie"]
print(etudiants)  # ['Alice', 'Bob', 'Charlie']

etudiants.append("Diana")
print(etudiants)  # ['Alice', 'Bob', 'Charlie', 'Diana']

etudiants.insert(1, "Eve")  # index 1, entre Alice et Bob
print(etudiants)  # ['Alice', 'Eve', 'Bob', 'Charlie', 'Diana']

etudiants.remove("Bob")
print(etudiants)  # ['Alice', 'Eve', 'Charlie', 'Diana']

dernier = etudiants.pop()
print(dernier)      # 'Diana'
print(etudiants)    # ['Alice', 'Eve', 'Charlie']





print(etudiants[0])  # 'Alice'
print(etudiants[2])  # 'Charlie'

print(etudiants[-1])  # 'Charlie'
print(etudiants[-2])  # 'Eve'