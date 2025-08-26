# cv.py

class Persoana:
    def __init__(self, nume, email):
        self.nume = nume
        self.email = email

class CV(Persoana):
    def __init__(self, nume, email, experienta):
        super().__init__(nume, email)
        self.experienta = experienta

    def afiseaza_cv(self):
        print(f"Nume: {self.nume}")
        print(f"Email: {self.email}")
        print("Experiență:")
        for job in self.experienta:
            print(f"- {job}")