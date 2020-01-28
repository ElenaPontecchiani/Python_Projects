#scrivo un dictionary di tutte le date di cpompleanno dei miei amici, poi quando inserisco nome utente stampo suo comple
import datetime
import json
#carico dictionary da file json e lo converto in dictionary, in seguito aggiungo un elemento

json_file = open("C:\\Users\\elepo\\PycharmProjects\\2-bDay\\bDayDictionary.txt", "r+")
friends_bday_dictionary = json.load(json_file)

#inseirmento nuovo nome
nome_da_inserire = input("Nome del nuovo amico: ")
compleanno_da_inserire = input("Compleanno del nuovo amico: ")
friends_bday_dictionary[nome_da_inserire] = compleanno_da_inserire

#print(friends_bday_dictionary)

nome = input("Nome: ")
if nome in friends_bday_dictionary:
    print(nome + " compie gli anni il giorno " + friends_bday_dictionary.get(nome))
else:
    print("Non è tuo amico")

#aggiornamento JSON: devo riaprire file in modalità scrittura, perchè con apertura
#precedente, anche se metto r+, il puntatore è in fondo al file, e quindi appende e basta
json_file2 = open("C:\\Users\\elepo\\PycharmProjects\\2-bDay\\bDayDictionary.txt", "w")
json.dump(friends_bday_dictionary, json_file2)

#ora creo un nuovo dictionary che per ogni mese dice quante persone nate in quel mese tra amici
count_mounth = {
    "January" : 0,
    "February" : 0,
    "March" : 0,
    "April" : 0,
    "May" : 0,
    "June" : 0,
    "July" : 0,
    "August" : 0,
    "September" : 0,
    "October" : 0,
    "November" : 0,
    "December" : 0,
}

for friend in friends_bday_dictionary:
    print(friend) #stampa chiavi
    print(friends_bday_dictionary[friend]) #stampa valore
    print(friends_bday_dictionary[friend].split(" ")[-2]) #stampa il mese
    month = int(friends_bday_dictionary[friend].split(" ")[-2])
    if month == 1:
        count_mounth["January"] +=1
    elif month == 2:
        count_mounth["February"] +=1
    elif month == 3:
        count_mounth["March"] +=1
    elif month == 4:
        count_mounth["April"] += 1
    elif month == 5:
        count_mounth["May"] +=1
    elif month == 6:
        count_mounth["June"] +=1
    elif month == 7:
        count_mounth["July"] +=1
    elif month == 8:
        count_mounth["August"] +=1
    elif month == 9:
        count_mounth["September"] +=1
    elif month == 10:
        count_mounth["October"] +=1
    elif month == 11:
        count_mounth["November"] +=1
    else:
        count_mounth["December"] +=1

print(count_mounth)

#grafico sulla frequenza dei compleanni nei vari mesi
import matplotlib.pyplot as plt
#import pandas as pd
import numpy as np

plt.hist(count_mounth.values(), None)
plt.xlabel("Mesi")
plt.ylabel("Numero compleanni")
plt.show()

