from django.urls import path

from . import views #perchè richiamiamo le funzioni che definiamo nelle view

app_name = 'polls'
urlpatterns = [
    #VUOL DIRE: SE QUALCUNO VA SUL NOSTRO SITO CHE SI CHIAMA, PER ESEMPIO, ELENA.COM, SENZA NIENTE (QUINDI SOLO ELENA.COM) VIENE INDIRIZZATO DALLA FUNZIONE INDEX DEL FILE VIEWS
    #NEL NOSTRO CASO: http://www.localhost:8000/polls/ SENZA NIENTE CHE SEGUE POLLS
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]