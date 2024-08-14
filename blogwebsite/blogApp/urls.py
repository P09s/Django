from django.urls import path,include
from .views import indexV
from . import views


urlpatterns = [
   path('', indexV, name='home'),
   path('login_user/', views.login_user, name='login'),
   path('signup/', views.signup_user, name='signup'),
   path('home/',views.home, name='home1'),
   # path('logout/',views.logout_user, name='logout'),
]