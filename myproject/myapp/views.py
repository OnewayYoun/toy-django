from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # name = 'Yoon'
    # context = {
    #     'last_name': 'Yoon',
    #     'age': 31,
    #     'nationality': 'Korea'
    # }
    # return render(request, 'index.html', {'last_name': name})
    # return render(request, 'index.html', context)
    return render(request, 'index.html')


def counter(request):
    # text = request.GET['text']    #GET 사용시
    text = request.POST['text']     #POST 사용시
    text_amount = len(text.split())

    return render(request, 'counter.html', {'amount': text_amount})