import logging
import math

print(dir(logging))
#le cose tutte in MAIUSC sono costanti
#quelle che iniziano in Maiusc sono classi
#quelli tutti in minusc sono f

#quello che facciamo noi è utilizzare il basicConfigMethod
#poi creiamo un Logger con il metodo getLogger

#1. Creo e configuro il logger, modulo che fa segnalazioni
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="C:\\Users\\elepo\\PycharmProjects\\0-hello\\errori.log", #attenzione carattere escape due volte \\
                    level = logging.DEBUG, #per settare l'importanza, di default è 30
                    format = LOG_FORMAT #settare il formato dell'errore, aggiungo data a quello di default
                    )
logger = logging.getLogger() #creo l'oggetto. non consigliato attribuirgli un nome personalizzato. Questo sarà il root logger


#2.  Test sul logger
logger.info("Our first message.")

#se faccio run ora il file è vuoto e non c'è il nostro messaggio. Ecco perchè:
print(logger.level)
#il livello è 30. Vuol dire che ogni livello dei log è asscociato a un valore numerico, nello specifico:
#noset:0, debug:10, info:20, warning:30, error:40, critic:50
#di default vengono scritti solo mex più grandi di 40, quindi vanno cambiate impostazioni settando il livello in basicConfig


#ora la uso per formula quadratica
def quadratic_formula (a,b,c):#Ritorna la soluzione dell'eq a*x^2+b*x+c
    logger.info("quadratic_formula ({0}, {1}, {2})".format(a,b,c))
    logger.debug("#Calcolo discriminate")
    delta = b**2 -4*a*c

    logger.debug("#Calcolo delle due radici")
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (b + math.sqrt(delta))/(2*a)

    logger.debug("#Ritorno le due radici come tuple")
    return (x1,x2)


radici = quadratic_formula(1,0,-4)
print(radici)




