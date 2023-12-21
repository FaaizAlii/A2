from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.SigninView.as_view(), name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.signout, name='logout'),
]