from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bank, Branch
from .forms import bankForm
from django.http import Http404
# Create your views here.


# name, description, inst_num, swift_code

class AddBank(LoginRequiredMixin, CreateView):
    template_name = 'banks/add_bank.html'
    model = Bank
    fields = ['name', 'institution_number', 'swift_code', 'description']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('banks:bank-detail', kwargs={'pk': self.object.pk})


class BankDetail(LoginRequiredMixin, DetailView):
    model = Bank
    template_name = 'banks/bank_details.html'
    context_object_name = 'bank'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise Http404("you don't have permission to access this page")
        return obj


class AddBranch(LoginRequiredMixin, CreateView):
    model = Branch
    template_name = 'banks/add_branch.html'
    fields = ['name', 'transit_number', 'address', 'email', 'capacity']

    def form_valid(self, form):
        bank_id = self.kwargs.get('pk')
        bank = get_object_or_404(Bank, pk=bank_id)

        form.instance.bank = bank
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('banks:branch-detail', kwargs={'pk': self.object.pk})


class BranchDetail(LoginRequiredMixin, DetailView):
    model = Branch
    template_name = 'banks/branch_details.html'
    fields = ['name', 'transit_number', 'email', 'capacity', 'address']
    context_object_name = 'branch'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        if obj.bank.owner != self.request.user:
            raise Http404("You don't have permission to access this page")

        return obj


class BranchEdit(LoginRequiredMixin, UpdateView):
    model = Branch
    template_name = 'banks/branch_edit.html'
    fields = ['name', 'transit_number', 'email', 'address', 'capacity']

    def get_success_url(self):
        return reverse_lazy('banks:branch-detail', kwargs={'pk': self.object.pk})


class AllBanks(ListView):
    model = Bank
    template_name = 'banks/all_banks.html'
    context_object_name = 'banks'
