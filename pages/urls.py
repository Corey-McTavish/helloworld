# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, coreyPageView, results, homePost, todos

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('corey/', coreyPageView, name='corey'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
    path('todos/', todos, name='todos'),
]
