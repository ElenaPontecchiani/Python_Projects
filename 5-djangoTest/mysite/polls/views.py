from django.http import HttpResponse
from .models import Question

#per importare template html
from django.template import loader
#per shortcut con render
from django.shortcuts import get_object_or_404, render

#per gestione err 404
from django.http import Http404


#LA FUNZIONE DICE CHE PAGINA VISUALIZZARE QUANDO VADO ALL'HOMEPAGE
#PER MAPPARE OGNI VISTA CON UNO SPECIFICO URL (NEL NOSTRO CASO http://localhost:8000/polls/)
#SERVE SPECIFICARLO NEL FILE url.py SEMPRE IN QUESTA CARTELLA, E IN urls.py CONTENUTO
#NELLA CARTELLA mysite/mysite

def index(request):
    #il segno meno in  -pub_date indica che l'ordine in cui le prendo è inverso, non c'entra con la sinatssi vera e propria della richiesta al db
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #constesto: racchiude tutte le var, aassociate a un nome, che voglio passare al mio file html. Vedi più info in commenti index.html
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



#in queste f come parametro passo anche question_id, perchè riferiscono a uno specifico el del db
#mentre il parametro request esiste sempre in qualsiasi richiesta!!


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)