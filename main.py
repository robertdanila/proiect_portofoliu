from cv import CV
from proiecte import Proiect, ProiectDetaliat
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

proiect2 = ProiectDetaliat(
    "Aplicatie Web",
    "Aplicatie Flask pentru portofoliu",
    "https://github.com/robertdanila/aplicatie_web",
    "Python + Flask"
)
proiect2.afiseaza_proiect()

print("\n---\n")

# === Contact ===
trimite_mesaj(
    nume="Andrei",
    email="andrei@email.com",
    mesaj="Salut! Interesant proiectul tau!"
)

print("\n=== Exemple dummy pentru ceilalti 3 piloni OOP ===")

# 1. Incapsulare
class ContBancar:
    def __init__(self, titular, sold):
        self.titular = titular      # atribut public
        self.__sold = sold          # atribut privat (encapsulat)

    def afiseaza_sold(self):
        print(f"Soldul contului pentru {self.titular} este {self.__sold} RON")

cont = ContBancar("Robert", 1000)
cont.afiseaza_sold()

# 2. Abstractie
from abc import ABC, abstractmethod

class Vehicul(ABC):
    @abstractmethod
    def porneste(self):
        pass

class Masina(Vehicul):
    def porneste(self):
        print("Masina porneste cu cheia")

class Bicicleta(Vehicul):
    def porneste(self):
        print("Bicicleta porneste prin pedalat")

masina = Masina()
bicicleta = Bicicleta()
masina.porneste()
bicicleta.porneste()

# 3. Polimorfism
class Animal:
    def vorbeste(self):
        print("Animalul scoate un sunet")

class Caine(Animal):
    def vorbeste(self):
        print("Ham Ham!")

class Pisica(Animal):
    def vorbeste(self):
        print("Miau Miau!")

animale = [Caine(), Pisica()]
for animal in animale:
    animal.vorbeste()

print("\n=== Modul interactiv ===")

# CV de la utilizator
nume_input = input("Introdu numele tau: ")
email_input = input("Introdu adresa de email: ")
exp_input = input("Adauga experiente (separate prin virgula): ").split(",")

cv_user = CV(nume_input, email_input, [e.strip() for e in exp_input if e.strip()])

print("\n--- CV-ul introdus ---")
cv_user.afiseaza_cv()

# Proiect de la utilizator
titlu_input = input("\nTitlul unui proiect: ")
descriere_input = input("Descrierea proiectului: ")
link_input = input("Link GitHub (optional): ")
tehnologie = input("Ce tehnologie folosesti: ")

proiect_user = ProiectDetaliat(titlu_input, descriere_input, link_input, tehnologie)

print("\n--- Proiectul introdus ---")
proiect_user.afiseaza_proiect()

# Mesaj de contact
print("\nFormular de contact:")
nume_msg = input("Nume expeditor: ")
email_msg = input("Email expeditor: ")
mesaj_msg = input("Mesaj: ")

trimite_mesaj(nume_msg, email_msg, mesaj_msg)

print("\n=== Sfarsit ===\n")