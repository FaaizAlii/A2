from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import FormView
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
# Create your views here.


class RegisterView(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)


class SigninView(LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('accounts:home')
    model = User
    template_name = 'accounts/login.html'


@never_cache
@login_required
def home(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/home.html')
    else:
        return redirect('accounts:login')


def signout(request):
    logout(request)
    return redirect(reverse('accounts:login'))
