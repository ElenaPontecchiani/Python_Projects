import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=32.71568000000008&lon=-117.16170999999997#.XicGSiPSI2w')

#dopo aver creato l'oggetto request lo uso con soup per avere un web scraping della pagina
#in questo modo saremo in grado di individuare, strutture, tag, capire come sono strutturti i file html, css..
soup = BeautifulSoup (page.content, 'html.parser')
print(soup)
#soup contiene tutto il contenuto della pagina html, css e gli script javascript


#se invece volessi trovare solo determinati tag dell'html:
print(soup.find_all("a"))

#ora cerco un preciso id per manipolarlo e farci cose
week = soup.find (id="seven-day-forecast-body")
print(week)
#l'ultimo print fa vedere quelll che ce dentro al div che chiedo

#ora voglio accedereagli elemnti dentro div
#per esempio noi vogliamo accedere a ogni casella del meteo all'interno del div
items = week.find_all(class_="tombstone-container")
print(items[0])
#ora uso get_text per avere solo il contenuto effettivo all'interno dei tag
print(items[0].find(class_="period-name").get_text())


#colleziono i period name in una struttura datu python
#in pratica sto dicendo: per ogni item che scorro dalla collezione items, faccio: item.find(class_="period-name").get_text()
#poi il risultato lo colleziono in period_name
period_name = [item.find(class_="period-name").get_text() for item in items]
short_description = [item.find(class_="short-desc").get_text() for item in items]
temperatures = [item.find(class_="temp").get_text() for item in items]
print(period_name)



#ora utilizzo pandas per strutturare le info che ho preso dalla pagina html
#la key del dictionary diventa il nome della colonna, ,mentre tutti i relativi valori saranno raggruppati sotto
#viene creata quindi una tabella
weather_stuff = pd.DataFrame(
    {"period name" : period_name,
     "short description" : short_description,
     "temperatures" : temperatures}
)

print(weather_stuff)

#scrittura su un file csv
weather_stuff.to_csv("Weather.csv")