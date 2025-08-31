class Proiect:
    def __init__(self, titlu, descriere, link):
        self.titlu = titlu
        self.descriere = descriere
        self.link = link

    def afiseaza_proiect(self):
        print(f"Titlu: {self.titlu}")
        print(f"Descriere: {self.descriere}")
        print(f"GitHub: {self.link}")


# Mostenire
class ProiectDetaliat(Proiect):
    def __init__(self, titlu, descriere, link, tehnologie):
        super().__init__(titlu, descriere, link)
        self.tehnologie = tehnologie   # atribut in plus

    def afiseaza_proiect(self):
        print(f"[DETALIAT] Titlu: {self.titlu}")
        print(f"Descriere: {self.descriere}")
        print(f"GitHub: {self.link}")
        print(f"Tehnologie: {self.tehnologie}")