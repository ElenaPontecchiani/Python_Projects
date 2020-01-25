'''
memoization fatta in due modi:
 -esplicitamente, per capire come funziona
 -attraverso il tool buildin in python
'''

#PRIMO APPROCCIO ESPLICITO
fibonacci_cache = {}

def fibonacci (n):
    #la prima cosa che faccio è vedere se il valore della serie n-esimo è salvato nella cache, e se è così lo ritorno
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    #se non è nella cache lo calcolo e lo metto in cache
    if n==1:
        value = 1
    elif n==2:
        value = 1
    elif n>2:
        value = fibonacci(n-1) + fibonacci(n-2)

    fibonacci_cache[n] = value
    return value


for n in range(1,11): #da 1..10
    print(n, ": ", fibonacci(n))


#SECONDO APPROCCIO AUTOMATIZZATO
from functools import lru_cache
@lru_cache(maxsize=1000)
def fibonacci2 (n):
    #anche gestione errori del tipo di dato in input, che deve essere int>0
    if type(n) != int:
        raise TypeError("n must be an integer")
    if n<1:
        raise ValueError("n must be equals or bigger than one")


    if n==1 or n==2:
        return 1
    elif n>2:
        return fibonacci(n-1) + fibonacci(n-2)


for i in range(1001):
    print(i, ": ", fibonacci2(i))