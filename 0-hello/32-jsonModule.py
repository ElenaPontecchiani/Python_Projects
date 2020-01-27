import json

'''
    json.load(f) : carica i dati nel JSON da un file 
    json.loads(s) : carica i dati del JSON da una stringa (è per questo che c'è una s alla fine del nome del metodo)
    json.dump(j,f) : scrive l'oggetto JSON su un file
    json.dumps(j) : scrive l'oggetto JSON su una stringa
'''

#FUNZIONE LOAD
json_file = open("C:\\Users\\elepo\\PycharmProjects\\0-hello\\movie_1.txt", "r", encoding="utf-8") #utf-8 per permettere anche caratteri non ASCII (esempio lettere straniere strane nei nomi dei tipi)
movie = json.load(json_file)
json_file.close()

#viene stampato simile a un dictionary
#notare che valori bool sono stati parsati correttamente da tru/false in True/False, cosi come null è diventato None
print(movie)
#infatti se ne visualizzo il tipo mi dice che è dictionary
print(type(movie))

#visto che è un dictionary posso accedere ai dati attraverso la key:
print(movie["title"])



#FUNZIONE LOADS
#creo una stringa (attenzione notazione di creazione su più righe) che contenga oggetto JSON
value = """{
	"title" : "Gattaca",
	"release_year" : 1997,
	"is_awsome" : true,
	"won_oscar" :false,
	"actors" : ["Ethan Hawke", "Uma Thurman", "Alan Arkin",
			"Loren Dean"],
	"budget" : null,
	"credits" : {
		"director" : "Andrew Niccol",
		"writer" : "Andrew Niccol",
		"composer" : "Micheal Nyman",
		"cinematographer" : "Slawomir Idziak"
		}
}
"""

tron = json.loads(value)
#anche qui tutti i dati parsati correttamente, None e boolean
print(tron)


#DUMPS:converte la stringa in un oggetto JSON che può essere inviato
print(json.dumps(movie))


#DUMP
movie2 = {}
movie2["title"] = "Minority Report"
movie2["director"] = "Spielberg"
movie2["composer"] = "Willimas"
movie2["actors"] = ["Cruise", "Farrell", "Von Sydow"]
movie2["is_awsome"] = True
movie2["budget"] = 1000000


json_file2 = open("C:\\Users\\elepo\\PycharmProjects\\0-hello\\movie_2.txt", "w", encoding="utf-8")
json.dump(movie2, json_file2)
json_file2.close()
