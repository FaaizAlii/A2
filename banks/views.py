from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bank,Branch
from .forms import bankForm
from django.http import Http404
# Create your views here.


# name, description, inst_num, swift_code

class AddBank( LoginRequiredMixin ,CreateView):
    template_name = 'banks/add_bank.html'
    model = Bank
    fields = ['name', 'institution_number', 'swift_code', 'description']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('banks:bank-detail', kwargs={'pk':self.object.pk})


class BankDetail(LoginRequiredMixin, DetailView):
    model = Bank
    template_name = 'banks/bank_details.html'
    context_object_name = 'bank'
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise Http404("you don't have permission to access this page")
        return obj

class AllBanks(ListView):
    model = Bank
    template_name = 'banks/all_banks.html'
    context_object_name = 'banks'
    # def get_queryset(self):
    #     obj = Bank.objects.all()
    #     return obj