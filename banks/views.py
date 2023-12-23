from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bank,Branch
from .forms import bankForm
# Create your views here.


# name, description, inst_num, swift_code

class AddBank( LoginRequiredMixin ,View):
    def get(self, request):
        form = bankForm()
        return render(request, 'banks/add_bank.html', {"form":form})
    
    def post(self, request):
        form = bankForm(request.POST)
        if form.is_valid():
            user = self.request.user
            name = form.cleaned_data.get('name')
            institution_number = form.cleaned_data.get('institution_number')
            swift_code = form.cleaned_data.get('swift_code')
            description = form.cleaned_data.get('description')
            
            Bank.objects.create(owner=user, name=name, institution_number=institution_number, swift_code=swift_code, description=description)
            messages.success(request, 'Bank Created Successfully!!')
            return redirect(reverse('banks:bank-detail'))

class BankDetail(View):
    def get(self, request):
        bank = Bank.objects.filter(owner = request.user)
        return render(request, 'banks/bank_details.html', {'bank':bank})