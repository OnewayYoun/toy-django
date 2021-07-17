from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # name = 'Yoon'
    context = {
        'last_name': 'Yoon',
        'age': 31,
        'nationality': 'Korea'
    }
    # return render(request, 'index.html', {'last_name': name})
    return render(request, 'index.html', context)