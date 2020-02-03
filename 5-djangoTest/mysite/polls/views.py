from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question

#per importare template html
from django.template import loader
#per shortcut con render
from django.shortcuts import get_object_or_404, render

from django.urls import reverse
from django.views import generic
#per gestione err 404
from django.http import Http404

from django.utils import timezone
#mi serve per il controllo pubblicazione domande che NON sia futura

#PRIMA
#LA FUNZIONE DICE CHE PAGINA VISUALIZZARE QUANDO VADO ALL'HOMEPAGE
#PER MAPPARE OGNI VISTA CON UNO SPECIFICO URL (NEL NOSTRO CASO http://localhost:8000/polls/)
#SERVE SPECIFICARLO NEL FILE url.py SEMPRE IN QUESTA CARTELLA, E IN urls.py CONTENUTO
#NELLA CARTELLA mysite/mysite


#DOPO:
#gestione con generic view

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """

        #__lte è una funzione usata per le datetime: datetimeinput__lte = altra_data
        #che permette di confrontare che datetimeinput sia precedente o uguale a altra_data
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

#in queste f come parametro passo anche question_id, perchè riferiscono a uno specifico el del db
#mentre il parametro request esiste sempre in qualsiasi richiesta!!


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.

        Deve escludere domande con date di pubblicazione non ammissibili (futuro)
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

#si arriva a questa vista quando seleziono una choice da vote
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

#funzione per votare la risposta alla domanda
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        #request.POST è un oggetto simile a un dictionary che permette di accedere ai dati
        #che confermo (in questo caso la scelta) attraverso la pk.
        #In questo caso request.POST['choice']  ritorna l'id della choice selezionata
        #come una stringa, dal momento che request.POST ha come valori sempre stinghe
        #volendo ci sarebbe la possibilità di fare la stessa azione con GET, ma noi la
        #facciamo con la POST perchè andiamo a modificare i dati nel MOdel

        #request.POST['choice']  è messa in un blocco try perchè lancia un errore se
        #l'utente non seleziona alcuna choice da fornire alla POST (quindi caso in cui
        #preme solo il bottone di conferma scelta senza realmente scegliere)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        #se tutto va bene aumento il count della choice, perchè un utente in più
        #l'ha scelta
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.


        #Invece di una solita HttpResponse uso HttpResponseRedirect, che prende
        #come argomento l'URL al quale l'utente viene inviato
        #Come sottolineato nel commento Python sopra, dovresti sempre restituire un
        # HttpResponseRedirect dopo aver gestito correttamente i dati POST.
        # Questo suggerimento non è specifico di Django; è una buona pratica di sviluppo Web in generale.


        '''
        COSA SUCCEDE NEL RETURN:
            -Il costruttore di HttpResponseRedirect prende un solo argomento: URL dove l'utente è reindirizzato
            -Tale argomento qui viene gestito con la funzione reverse(). La funzione serve a evitare di avere l'URL
             hard-coded nella funzione. A tale funzione serve il nome della view alla quale voglio passare il controllo
             e la parte variabile del pattern URL che punta a quella vista.
             Nel nostro caso, usando urlconf prima settato, la funzione reverse creerà una stringa del tipo:
             /polls/3/results/
             dove 3 è il valore di una question.id
        '''
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))