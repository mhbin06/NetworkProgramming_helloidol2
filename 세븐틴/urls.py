from django.urls import path

from 세븐틴 import views

app_name = '세븐틴'


urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character_list'),
]