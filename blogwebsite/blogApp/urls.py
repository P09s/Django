from django.urls import path,include
from .views import indexV

urlpatterns = [
    path('index/', indexV)
]