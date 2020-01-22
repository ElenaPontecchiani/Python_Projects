def translate (phrase):
    translation = "" #il risultato finale per ora uguale alla stringa vuota
    #loop che fa la seguente cosa: scorre tutta la frase, se è vocale la cambia in g, altrimenti lascia cosi
    for i in phrase:
        if i.lower() in "aeiou":
            if i.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += i
    return translation

phrase = input("Initial phrase= ")
print(translate(phrase))
