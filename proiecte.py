class Proiect:
    def __init__(self, titlu, descriere, link):
        self.titlu = titlu
        self.descriere = descriere
        self.link = link

    def afiseaza_proiect(self):
        print(f"Titlu: {self.titlu}")
        print(f"Descriere: {self.descriere}")
        print(f"GitHub: {self.link}")
