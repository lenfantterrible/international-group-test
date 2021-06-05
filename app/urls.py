from django.contrib import admin
from django.urls import path
from .views import FiboView, AckermanView, FactView, HomeView

app_name = 'app'

urlpatterns = [

    path('fibonacci/', FiboView.as_view(), name='fibonacci'),
    path('ackerman/', AckermanView.as_view(), name='ackerman'),
    path('factorial/', FactView.as_view(), name='factorial'),
    path('', HomeView.as_view(), name='home'),


]
