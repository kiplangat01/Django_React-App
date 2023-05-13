from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from .models import Post
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context )

def about(request):
    return render(request ,'blog/about.html')


def register(request):
    if request.method == 'POST':
       form = UserRegisterForm(request.POST)
       if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has beem created for {username}!')
            return redirect('blog-home')
    else:
       form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form':form})


@login_required
def profile(request): 
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           messages.success(request, f'Your Account has beem updated! ')
           return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'blog/profile.html', context)

