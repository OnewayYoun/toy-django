from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages

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
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Yoon'
    # feature1.details = 'Hi! I"m Yoon'
    # feature1.is_true = True
    #
    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Kim'
    # feature2.details = 'Hi! I"m Kim'
    # feature2.is_true = True
    #
    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Lee'
    # feature3.details = 'Hi! I"m Lee'
    # feature3.is_true = False
    #
    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'Park'
    # feature4.details = 'Hi! I"m Park'
    # feature4.is_true = True
    #
    # features = [feature1, feature2, feature3, feature4]

    features = Feature.objects.all()    #getting all data(objects) from DB
    return render(request, 'index.html', {'features': features})


def counter(request):
    # text = request.GET['text']    #GET 사용시
    text = request.POST['text']  # POST 사용시
    text_amount = len(text.split())

    return render(request, 'counter.html', {'amount': text_amount})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('index')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    else:
        return render(request, 'register.html')
