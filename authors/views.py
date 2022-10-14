from django.http.response import Http404
from django.shortcuts import render

from .forms import RegisterForm


# Create your views here.
def register_view(request):
    form = RegisterForm()
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })


def register_create(request):
    if not request.POST:
        raise Http404()

    form = RegisterForm()
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
    })
