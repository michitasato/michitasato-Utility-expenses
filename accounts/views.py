from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm


def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'data': data,
    }
    return render(request, 'accounts/index.html', params)

def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/accounts')
    params = {
        'title': 'Hello',
        'form': FriendForm(),
    }
    return render(request, 'accounts/create.html', params)

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/accounts')
    params = {
        'title': 'Hello',
        'id': num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'accounts/edit.html', params)
