from django.urls import path
from . import views

app_name = 'banks'

urlpatterns = [
    path('all/', views.AllBanks.as_view(), name='all'),
    path('add/', views.AddBank.as_view(), name='add'),
    path('<int:pk>/branches/add/', views.AddBranch.as_view(), name='add-branch'),
    path('<int:pk>/details/', views.BankDetail.as_view(), name='bank-detail'),
    path('branch/<int:pk>/details/', views.BranchDetail.as_view(), name='branch-detail'), #/banks/branch/<branch_id>/details/
    path('branch/<int:pk>/edit/', views.BranchEdit.as_view(), name='branch-edit'), #/banks/branch/<branch_id>/edit/

]