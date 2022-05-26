from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

def SignUpView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
   
    form = SignUpForm()
    print(form.has_error)
    context = {
        "forms":form
    }

    return render(request, 'users/sign_up.html', context)
