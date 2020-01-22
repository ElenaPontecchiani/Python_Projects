#var che memorizza la parola segreta, che definisce il programma
secret_word = "giraffe"

#creo una variabile che memorizza le risposte dell'utente
guess = ""

#metto un numero limite di tentativi
i = 0

while i < 3 and guess != secret_word :
    guess = input ("Enter the word: ")
    i += 1

if i<3:
    print("You win")
else:
    print("You lost")

