#scrivo una lambda che dati in input nome e cognome separati presi da una pagina web li visualizza insieme

f = lambda name, surname : name.strip().title() + " " + surname.strip().title()

print(f("ele", "PONTI"))

'''altro esempio: uso lambda per ordinare lista. la lista di autori deve essere ordinata per il cognome.
   Per farlo: al sort passo come parametro una f lambda che dice che prendo ultimo valore stringa senza contare lo spazio
'''

authors = ["Isaac Newton", "Isaac Asymov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke", "Orson Scott card"]
authors.sort(key = lambda name: name.split(" ")[-1].lower())
print(authors)

'''ALTRO ESEMPIO: uso lambda quando voglio ritornare una funzione'''
def build_quadratic_function(a,b,c):
    return lambda x: a*x**2+b*x+c

f= build_quadratic_function(5,3,2)
print(f(0))
print(build_quadratic_function(5,3,2)(0))