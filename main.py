# main.py

from cv import CV
from proiecte import Proiect
from contact import trimite_mesaj

# === CV ===

# Cream o variabila 'cv' de tipul clasei CV
cv = CV(
    "Robert Danila",
    "robert.danila@email.com",
    ["IT Support - 2 ani", "Junior Python Dev - 1 an"]
)

cv.afiseaza_cv()

# === Tipuri de date primitive (str, list, int, float, bool) ===
# str -> nume/email (deja folosite mai sus)
varsta = 30               # int
rating_portofoliu = 4.8   # float
disponibil = True         # bool

print(f"\nProfil: varsta={varsta} (int), rating={rating_portofoliu} (float), disponibil={disponibil} (bool)")

# === Structuri de date ===

# list (indexata, ordonata, modificabila, permite duplicate)
experiente = ["IT Support - 2 ani", "Junior Python Dev - 1 an"]

# tuple (indexata, ordonata, nemodificabila, permite duplicate)
coordonate = (45.76, 21.23)

# set (neindexat, neordonat, modificabil, fara duplicate)
tehnologii = {"Python", "Flask", "SQLite"}

# dict (indexat prin cheie, ordonat, modificabil, cheile unice)
proiect_info = {
    "titlu": "Site Portofoliu",
    "limbaj": "Python",
    "an": 2025
}

print("\nStructuri de date din proiect:")
print("Lista experiente:", experiente)
print("Tuplu coordonate:", coordonate)
print("Set tehnologii:", tehnologii)
print("Dictionar proiect:", proiect_info)


if disponibil and rating_portofoliu >= 4.5:
    print("Esti disponibil si ai un rating foarte bun.")
elif disponibil:
    print("Esti disponibil pentru proiecte.")
else:
    print("Momentan esti indisponibil.")

if varsta >= 18:
    print("Esti major, poti incheia colaborari.")
else:
    print("Esti minor.")

# === if / elif / else ===
if len(cv.experienta) == 0:
    print("Nu ai inca experienta profesionala.")
elif len(cv.experienta) == 1:
    print("Ai un job anterior.")
else:
    print("Ai experienta profesionala solida.")

# === for + continue ===
print("\nExperienta avansata (excludem pozitiile 'Junior'):")
for job in cv.experienta:
    if "Junior" in job:
        continue
    print(f"- {job}")

# === while + break ===
print("\nCautare primul job 'Junior' (while + break):")
i = 0
gasit = False
while i < len(cv.experienta):
    if "Junior" in cv.experienta[i]:
        print(f"Gasit: {cv.experienta[i]}")
        gasit = True
        break
    i += 1
if not gasit:
    print("Nu exista job 'Junior' in lista.")

print("\n---\n")

# === Proiecte ===
proiect1 = Proiect(
    "Site Portofoliu",
    "Aplicatie Python pentru prezentare CV si proiecte",
    "https://github.com/robert/portofoliu"
)
proiect1.afiseaza_proiect()

print("\n---\n")

# === Contact ===
trimite_mesaj(
    nume="Andrei",
    email="andrei@email.com",
    mesaj="Salut! Interesant proiectul tau!"
)
