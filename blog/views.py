from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm
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
    return render(request, 'blog/profile.html')

