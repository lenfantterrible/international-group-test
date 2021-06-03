from django.contrib import admin
from django.urls import path
from .views import fibonacci, ackerman

app_name = 'app'

urlpatterns = [

    path('fibonacci/', fibonacci, name='fibonacci'),
    path('ackerman/', ackerman, name='ackerman'),

]
