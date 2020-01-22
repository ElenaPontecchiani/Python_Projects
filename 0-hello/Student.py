#modello la classe studente
class Student:
    def __init__(self, nome, cognome, matricola, facolta, in_corso):
        self.nome=nome
        self.cognome = cognome
        self.matricola = matricola
        self.facolta = facolta
        self.in_corso = in_corso

    def is_science_honor(self): #se fa facoltà scientifica ed è in corso
        if (self.facolta == "Informatica" or self.facolta == "Scienze") and (self.in_corso==True):
            return True
        else:
            return False
