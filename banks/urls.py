from django.urls import path
from . import views

app_name = 'banks'

urlpatterns = [
    path('add/', views.AddBank.as_view(), name='add'),
    path('<int:pk>/details/', views.BankDetail.as_view(), name='bank-detail'), # success url = /banks/<bank_id>/details/

]