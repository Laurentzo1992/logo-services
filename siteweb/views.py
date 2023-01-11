from multiprocessing import context
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'siteweb/base.html', context)

# Create your views here.
