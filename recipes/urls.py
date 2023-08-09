from recipes.views import home, about, contact
from django.urls import path


urlpatterns = [
    path('', home), #home
    path('about/', about), #sobre
    path('contact/', contact) #contato
]
