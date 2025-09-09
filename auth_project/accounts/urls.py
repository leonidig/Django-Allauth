from django.urls import path

from .views import index

app_name = 'accounts'


urlpatterns = [
    path('profile/', index, name='index'),
]

