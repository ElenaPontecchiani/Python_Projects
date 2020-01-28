#get the python version i'm using
import sys #system specif parameters and function
print(sys.version)

#display current date and time
import datetime
print(datetime.datetime.today())

#circle area
import math
r = int(input("insert radius: "))
print("The area is: ", str(r**2*math.pi))

#converto stringa in input con valori numerici separati solo da , in lista e tupla
numbers = input("input: ")
list =numbers.split(",")
print(list)
tupla = tuple(list)
print(tupla)

#utente inserisce nome del file e stampo la sua estensione
filename = input("Filename: ")
print(filename.split("."))
print(filename.split(".")[-1])


#scrittura data (sempre in stringa) da 31 12 1998 a 31/12/1998
date_as_string = (31,12,98)
print("%i / %i / %i" %date_as_string)

#programma che stampa il calendario (giorni mese-giorni settimana) del mese dell'anno dati in input, uso pack calendar
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
#ATTENZIONE CHE SI DEVE CONVERTIRE IN INPUT
print(calendar.month(y, m))

#calcolo dei giorni di ditanza tra due date
import datetime
date1 = datetime.date(1998,4,28)
date2 = datetime.date(1992,7,29)
delta = date1-date2
print("The difference is: ", delta.days, "days")

#funzione che valuta se un certo file esiste
import os.path
open('abc.txt', 'w')
print(os.path.isfile('abc.txt')) #True perchè con w lo creo
open('abc.txt', 'r')
print(os.path.isfile('def.txt'))#False perchè con r dovrei leggere un file già esistente

#vedere info sul sistema operativo su cui python sta andando
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())


#vedere info sul file correntemente aperto
import os
print("Current File Name : ",os.path.realpath(__file__))

#vedere numero di cpu che sto usando
import multiprocessing
print(multiprocessing.cpu_count())


#stampare statistiche uso python
import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')


#ordinare file in base alla data di creazione
import glob
import os
files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))

#f di hash per una parola casuale
soundex = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]
word = input("Input the word be hashed: ")
word = word.upper()
coded = word[0]
for a in word[1:len(word)]:
    i = 65 - ord(a)
    coded = coded + str(soundex[i])
print()
print("The coded word is: " + coded)
print()

#script che dice quanti moduli built in sono disponibili
import sys
import textwrap
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))


#f che ritorna la taglia di un oggetto in byte
import sys
str1 = "one"
str2 = "four"
str3 = "three"
print()
print("Memory size of '"+str1+"' = "+str(sys.getsizeof(str1))+ " bytes")
print("Memory size of '"+str2+"' = "+str(sys.getsizeof(str2))+ " bytes")
print("Memory size of '"+str3+"' = "+str(sys.getsizeof(str3))+ " bytes")
print()

#f che ritorna la dimensione di un file
import os
file_size = os.path.getsize("abc.txt")
print("\nThe size of abc.txt is :",file_size,"Bytes")
print()


#f che dice nome dell'host attraverso il pack socket
import socket
host_name = socket.gethostname()
print()
print("Host name:", host_name)
print()
