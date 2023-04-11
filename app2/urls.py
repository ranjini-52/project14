from django.urls import path
from app2.views import *
app_name='country2'
urlpatterns=[
    path('pakistan/',pakistan,name='pakistan'),
]
app_name='country4'
urlpatterns=[
    path('russia/',russia,name='russia'),
]