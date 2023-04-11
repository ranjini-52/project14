from django.urls import path
from app1.views import *
app_name='country1'
urlpatterns=[
    path('india/',india,name='india'),
]
app_name='country3'
urlpatterns=[
    path('america/',america,name='america'),
]