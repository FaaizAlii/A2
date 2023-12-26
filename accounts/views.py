from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import FormView
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
from .forms import UserProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import make_password
from banks.models import Bank, Branch

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
    template_name = 'accounts/login.html'
    
    def get_success_url(self):
        # return '/accounts/profile/'
        return reverse_lazy('accounts:profile')


@never_cache
@login_required(login_url='accounts:login')
def home(request):
    banks = Bank.objects.filter(owner=request.user)
    return render(request, 'accounts/home.html', {"banks": banks})


@login_required
def profileView(request):
    if request.user.is_authenticated:
        user = request.user
        profile_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
        return JsonResponse(profile_data)
    else:
        return redirect('accounts:login')


@login_required
def profileEdit(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            old_pass = request.user.password
            new_pass1 = form.cleaned_data.get('password1')
            if not new_pass1:
                current_user = User.objects.get(id=request.user.id)
                current_user.first_name = request.POST.get('first_name')
                current_user.last_name = request.POST.get('last_name')
                current_user.email = request.POST.get('email')
                current_user.save()
                messages.success(request, "info updated Successfully!")
                return redirect(reverse('accounts:profile'))
            else:
                new_pass2 = form.cleaned_data.get('password2')
                if new_pass1 == new_pass2 and len(new_pass1) >= 8:
                    new_pass1 = make_password(new_pass1)
                    if new_pass1 == old_pass:
                        messages.error(
                            request, "new password must not be same as old password!")
                        return redirect('accounts:edit')
                    else:
                        current_user = User.objects.get(id=request.user.id)
                        current_user.first_name = request.POST.get(
                            'first_name')
                        current_user.last_name = request.POST.get('last_name')
                        current_user.email = request.POST.get('email')
                        current_user.set_password(new_pass2)
                        current_user.save()
                        update_session_auth_hash(request, current_user)
                        messages.success(request, "info updated Successfully!")
                        return redirect(reverse('accounts:profile'))
                else:
                    messages.error(
                        request, "invalid Password! remember lenth must not be less than 8 and both passwords should match!")
                    return redirect('accounts:edit')
        else:
            messages.error(request, 'incorrect info please try again')
            return redirect('accounts:edit')

    form = UserProfileForm(instance=request.user)
    return render(request, 'accounts/profile_edit.html', {'form': form})


def signout(request):
    logout(request)
    return redirect(reverse('accounts:login'))
