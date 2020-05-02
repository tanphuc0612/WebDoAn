from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print('correct')
            return redirect('register-success')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form},)

# [test login] test login success
def register_success(request):
    return render(request, template_name='home.html')

@login_required
def profile(request):
    return render(request, 'profile.html')