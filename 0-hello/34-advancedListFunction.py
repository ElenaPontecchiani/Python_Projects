#MAP: esempio voglio convertire da Celsius a Farhenait

temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19),
         ("Los Angeles", 26), ("Tokyo", 27), ("New York", 28),
         ("London", 22), ("Beijin", 32),
         ]

#f di conversione la faccio con una lambda: nome rimane invariato, la f di conversione è applicata all'ultimo valore
c_to_f = lambda data: (data[0], (9/5)*data[1] +32)
print(list(map(c_to_f,temps)))

#FILTER: serve per selezionare parte di dati da una lista/tupla/dato iterabile
#per arricchire l'esempio voglio filtrare tutti i dato >=mean, che appartiene al pack statisic
import statistics
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)
print(list(filter(lambda x: x>=avg, data)))

#REDUCE: NON ESISTE PIU' IN PYTHON>3 LOL