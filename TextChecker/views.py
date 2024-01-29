from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.views.generic import TemplateView
from .models import User


def Text(request):
      all_users = User.objects.all
      if request.method == 'POST':
            form = SignUpForm(request.POST or None)
            if form.is_valid():
                  form.save()
                  messages.success(request, ('form submitted successfully'))
                  return render(request, 'TextChecker\Thanks.html', {'all': all_users,})
            else:
                  messages.success(request, 'error in form')
                  return render(request, 'TextChecker\home.html', {'all': all_users,})
            
      else:
          form = SignUpForm()
      return render(request, 'TextChecker\home.html', {})
        
