from django.urls import path
from . import views



urlpatterns = [
    path('cards/', views.cards, name='cards'),
    path("",views.base,name='base'),
    path('add_items_form/',views.add_items_form, name='add_form'),
       
            
    ]    





