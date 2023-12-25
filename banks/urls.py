from django.urls import path
from . import views

app_name = 'banks'

urlpatterns = [
    path('all/', views.AllBanks.as_view(), name='all'),
    path('add/', views.AddBank.as_view(), name='add'),
    # path('<int:pk>/branches/add/', views.AddBank.as_view(), name='add-branch'),
    path('<int:pk>/details/', views.BankDetail.as_view(), name='bank-detail'),

]