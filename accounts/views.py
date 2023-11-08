from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()                                # edite esta linha
            user_group = Group.objects.get(name='basic_user') # edite esta linha
            user.groups.add(user_group)                       # edite esta linha

            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)
