from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserForm


def all_users(request):
    """ A view to show all Users """

    users = User.objects.all()

    context = {
        'users': users,
    }

    return render(request, 'users/users.html', context)
