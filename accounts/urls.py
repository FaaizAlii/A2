from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.SigninView.as_view(), name='login'),
    path('profile/', views.home, name='profile'),
    path('profile/view/', views.profileView, name='view'),
    path('profile/edit/', views.profileEdit, name='edit'),
    path('logout/', views.signout, name='logout'),
]