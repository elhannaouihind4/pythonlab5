notes = [12, 15, 9, 18, 14, 16]

print(notes[1:4])   # [15, 9, 18]
print(notes[:3])    # [12, 15, 9]  (début implicite 0)
print(notes[3:])    # [18, 14, 16] (fin implicite len)
print(notes[::2])   # [12, 9, 14]   (un élément sur deux)
print(notes[::-1])  # [16, 14, 18, 9, 15, 12] (liste inversée)
print(notes[:])