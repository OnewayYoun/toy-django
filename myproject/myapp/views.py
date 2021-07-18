from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    # name = 'Yoon'
    # return render(request, 'index.html', {'last_name': name})

    # context = {
    #     'last_name': 'Yoon',
    #     'age': 31,
    #     'nationality': 'Korea'
    # }
    # return render(request, 'index.html', context)

    # Models
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Yoon'
    feature1.details = 'Hi! I"m Yoon'

    return render(request, 'index.html', {'feature': feature1})


def counter(request):
    # text = request.GET['text']    #GET 사용시
    text = request.POST['text']  # POST 사용시
    text_amount = len(text.split())

    return render(request, 'counter.html', {'amount': text_amount})
