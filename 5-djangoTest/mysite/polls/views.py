from django.http import HttpResponse

#LA FUNZIONE DICE CHE PAGINA VISUALIZZARE QUANDO VADO ALL'HOMEPAGE
#PER MAPPARE OGNI VISTA CON UNO SPECIFICO URL (NEL NOSTRO CASO http://localhost:8000/polls/)
#SERVE SPECIFICARLO NEL FILE url.py SEMPRE IN QUESTA CARTELLA, E IN urls.py CONTENUTO
#NELLA CARTELLA mysite/mysite

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")