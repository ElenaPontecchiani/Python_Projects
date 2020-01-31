from django.urls import path

from . import views #perchè richiamiamo le funzioni che definiamo nelle view


urlpatterns = [
    #VUOL DIRE: SE QUALCUNO VA SUL NOSTRO SITO CHE SI CHIAMA, PER ESEMPIO, ELENA.COM, SENZA NIENTE (QUINDI SOLO ELENA.COM) VIENE INDIRIZZATO DALLA FUNZIONE INDEX DEL FILE VIEWS
    #NEL NOSTRO CASO: http://www.localhost:8000/polls/ SENZA NIENTE CHE SEGUE POLLS
    path('', views.index, name='index'),
]