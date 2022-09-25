from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Bu elektron poçt üçün hesab yaradıldı: {email}! Artıq hesabınıza daxil ola bilərsiniz')
            return redirect('login')
        messages.error(request, "Uğursuz qeydiyyat. Daxil etdiyiniz məlumatları yenidən yoxlayın.")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)  # <-- Here if the remember me is False, that is why expiry is set to 0 seconds. So it will automatically close the session after the browser is closed.
                messages.success(request, 'Hesabınıza uğurla daxil oldunuz!')
                return redirect('client-home')
        messages.error(request, "Uğursuz giriş. Daxil etdiyiniz məlumatları yenidən yoxlayın.")
        form = UserLoginForm()
        render(request, 'users/login.html', {'form': form})
    else:
        form = UserLoginForm()
        render(request, 'users/login.html', {'form': form})

