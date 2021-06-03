from django.contrib import admin
from django.urls import path
from .views import fibonacci, ackerman, factorial, HomeView

app_name = 'app'

urlpatterns = [

    path('fibonacci/', fibonacci, name='fibonacci'),
    path('ackerman/', ackerman, name='ackerman'),
    path('factorial/', factorial, name='factorial'),
    path('', HomeView.as_view(), name='home'),


]
