from django.urls import path

from . import views #perchè richiamiamo le funzioni che definiamo nelle view


urlpatterns = [
    #VUOL DIRE: SE QUALCUNO VA SUL NOSTRO SITO CHE SI CHIAMA, PER ESEMPIO, ELENA.COM, SENZA NIENTE (QUINDI SOLO ELENA.COM) VIENE INDIRIZZATO DALLA FUNZIONE INDEX DEL FILE VIEWS
    #NEL NOSTRO CASO: http://www.localhost:8000/polls/ SENZA NIENTE CHE SEGUE POLLS
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]