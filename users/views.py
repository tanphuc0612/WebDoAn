from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('register-success')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form},)

# [test login] test login success
def home(request):
    return render(request, template_name='home.html')


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(Profile, pk=self.request.user.id)